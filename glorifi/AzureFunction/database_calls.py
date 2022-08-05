import logging
import shared_code.settings as settings
import shared_code.valid_params as valid_params
import requests
import json
import traceback
from sqlite3 import Cursor
from typing_extensions import Required
from datetime import date, datetime
from xmlrpc.client import Boolean
import psycopg2
import logging
from psycopg2.extras import RealDictCursor, DictCursor
import shared_code.settings as settings

def calculate_age(born):
    born = datetime.strptime(born, '%m/%d/%Y')
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def return_connection():
    try:
        conn = psycopg2.connect(host=settings.POSTGRESS_HOST, database=settings.POSTGRESS_DB_NAME, user=settings.POSTGRESS_USER,password=settings.POSTGRESS_DB_PASSWORD,port=settings.POSTGRESS_DB_PORT, cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        conn.set_session(autocommit=True)
        logging.info('Database connection was successful!')
        conn.set_session(autocommit=True)
        return cursor, conn
    except Exception as error:
       logging.error('Connecting to Database failed')
       logging.error('Error: {}'.format(error))

def call_pg_function(pg_fn_name, param_list, fetchall=True):
    """
    This is a common function which is used to call the Postgres function
    pg_fn_name: Postgres Function name
    param_list: Input Paramaters
    """
    sql_call_status = True
    output = None
    logging.info("Started executing postgres function: {0}".format(pg_fn_name))
    cursor, conn = return_connection()
    try:
        cursor.callproc(pg_fn_name, param_list)
        if fetchall:
            output = cursor.fetchall()
        else:
            output = cursor.fetchone()
    except Exception as e:
        logging.error("Exception occured while executing postgres function:" + traceback.format_exc())
        sql_call_status = False
    finally:
        if conn.closed == 0:
            conn.close()
        cursor.close()
        del cursor
        logging.info('Database Connection Closed')
        logging.info("Ended executing postgres function: {0}".format(pg_fn_name))
        return sql_call_status, output

def get_item_access_token(item_id):
    access_token = False
    try:
        status, access_token = call_pg_function('datahub.plaid_get_item_access_token', [item_id], False)
        if status:
            logging.info("SQL statement successfully executed")
            access_token = access_token['plaid_access_token']
            logging.info("access_token: {0}".format(access_token))
        else:
            logging.error("SQL Failed")
    except Exception as e:
        logging.error("Exception occured while executing get_item_access_token:" + traceback.format_exc())
    finally:
        logging.info("Ended executing get_item_access_token")
        return access_token

def check_item_id_existance(item_id:str=None)->Boolean:

    item_exist = False
    try:
        status, item_exist = call_pg_function('datahub.check_item_id_existance', [item_id], False)
        if status:
            logging.info("SQL statement successfully executed")
            item_exist = item_exist['check_item_id_existance']
            logging.info("item_exist: {0}".format(item_exist))
    except Exception as e:
        logging.error("Exception occured while executing function: check_item_id_existance\n" + traceback.format_exc())
    finally:
        return item_exist

def update_item_table_error_status(item_id:str=None,
payload:dict={})->Boolean:
    status = 'error'
    update_status = False
    try:
        error_json = json.dumps(payload.get('error'), default=str)
        update_status, updated_id = call_pg_function('datahub.plaid_update_item_table_error_status', [item_id, status, error_json], False)
        if update_status:
            logging.info("Updated successfully")
            updated_id = updated_id["id"]
            logging.info("updated_id: {0}".format(updated_id))
        else:
            logging.error("Update failed")
    
    except Exception as e:
        logging.error("Exception occured while executing function: update_item_table_error_status\n" + traceback.format_exc())

    finally:
        return update_status

def update_item_table_expiration_status(item_id: str = None) -> Boolean:

    status = 'pending'
    update_status = False
    try:
        update_status, updated_id = call_pg_function('datahub.plaid_update_item_table_expiration_status', [item_id, status], False)
        if update_status:
            logging.info("Updated successfully")
            updated_id = updated_id["id"]
            logging.info("updated_id: {0}".format(updated_id))
        else:
            logging.error("Update failed")
    
    except Exception as e:
        logging.error("Exception occured while executing function: update_item_table_expiration_status\n" + traceback.format_exc())

    finally:
        return update_status

def insert_account(accounts, item_id):
    """Table Columns
    item_id, plaid_account_id, name, mask, official_name, current_balance,
    available_balance, iso_currency_code, unofficial_currency_code, type,
    subtype, raw_json
    """
    item_id_arr = []
    account_id_arr = []
    subtype_arr = []
    status_arr = []
    account_name_arr = []
    mask_arr = []
    official_name_arr = []
    current_bal_arr = []
    available_bal_arr = []
    iso_curr_arr = []
    type_arr = []
    raw_json_arr = []
    try:
        for account in accounts:
            try:
                item_id_arr.append(item_id)
                status_arr.append('good')
                account_id_arr.append(account.get("account_id"))
                subtype_arr.append(str(account.get("subtype")))
                account_name_arr.append(str(account.get("name")))
                mask_arr.append(str(account.get("mask")))
                official_name_arr.append(str(account.get("official_name")))
                type_arr.append(str(account.get("type")))
                raw_json_arr.append(json.dumps(account.to_dict(), default=str))
                current_bal_arr.append(float(account.get(
                                            'balances', {}).get('current', None)))
                iso_curr_arr.append(str(account.get(
                                            'balances', {}).get('iso_currency_code', None)))
                available_bal_arr.append(float(account.get(
                                            'balances', {}).get('available', None)))
            except:
                continue
        status, _ = call_pg_function('datahub.post_plaid_account', [item_id_arr, account_id_arr, subtype_arr, status_arr, account_name_arr, mask_arr, official_name_arr, current_bal_arr, available_bal_arr, iso_curr_arr, type_arr, raw_json_arr])
        if status:
            logging.info('Accounts Added')
        else:
            logging.info('Adding accounts failed')
    except Exception as e:
        logging.error("Exception occured while executing function: update_item_table_expiration_status\n" + traceback.format_exc())

def update_account(account:dict={})->Boolean:
    """Table Columns
    plaid_account_id, name, mask, official_name, current_balance,
    available_balance, iso_currency_code, unofficial_currency_code, type,
    subtype, raw_json
    """
    #: Get the required column values. 
    #: If key not present, add default as None
    plaid_account_id = str(account.get('account_id',None))
    name = str(account.get('name',None))
    mask = str(account.get('mask',None))
    official_name = str(account.get('official_name', None))
    current_balance = account.get(
        'balances', {}).get('current', None)
    available_balance = account.get(
        'balances', {}).get('available', None)
    iso_currency_code = str(account.get(
        'balances', {}).get('iso_currency_code', None))
    uof_c_code = str(account.get('balances', {}).get(
        'unofficial_currency_code', None))
    _type = str(account.get('type',None))
    subtype =str(account.get('subtype', None))
    raw_json = json.dumps(account.to_dict(), default=str)

    logging.info("Updating with the below data, where plaid_account_id: {0}".format(plaid_account_id))
    logging.info(
        """plaid_account_id: {0}\n name: {1}\n mask: {2}\n official_name: {3}\n current_balance: {4}\n
        available_balance: {5}\n iso_currency_code: {6}\n uof_c_code: {7}\n _type: {8}\n subtype: {9}\n raw_json: {10}"""
        .format(
            plaid_account_id, name, mask, official_name, current_balance,
            available_balance, iso_currency_code, uof_c_code, _type, subtype, raw_json
        )
    )

    acc_update_status, acc_update_op = call_pg_function(
            'datahub.patch_plaid_accounts_table', 
            [
                plaid_account_id, name, mask, official_name, 
                current_balance, available_balance, iso_currency_code,
                uof_c_code, _type, subtype, raw_json
            ],
            False)
    if acc_update_status:
        logging.info("Updated member account information successfully")
        acc_updated_row_id = acc_update_op["id"]
        logging.info("Updated row ID: {0}".format(acc_updated_row_id))
    else:
        logging.error("SQL Failed while updating plaid_account_id: {0}".format(plaid_account_id))
    
    return acc_update_status

def plaid_item_status_update(item_id:str=None)->Boolean:
    status = 'unlinked'
    update_status = False
    try:
        update_status, updated_id = call_pg_function('datahub.plaid_item_status_update', [item_id, status], False)
        if update_status:
            logging.info("Updated successfully")
            updated_id = updated_id["id"]
            logging.info("updated_id: {0}".format(updated_id))
        else:
            logging.error("Update failed")
    
    except Exception as e:
        logging.error("Exception occured while executing function: plaid_item_status_update\n" + traceback.format_exc())

    finally:
        return update_status

def insert_transactions(transactions):
    logging.info("Transactions Insertion Begining. Number of transactions to insert: %d", len(transactions))
    for transaction in transactions:
        account_id = transaction['account_id']
        plaid_transaction_id = transaction['transaction_id']
        plaid_category_id = transaction['category_id']
        category = transaction['category'][0]
        try:
            subcategory = transaction['category'][1]
        except:
            subcategory = 'NONE'
        amount = transaction['amount']
        date_ = transaction['date']
        pending = transaction['pending']
        transaction = json.dumps(transaction.to_dict(), default=str)
        transaction_insert_status, transaction_insert_op = call_pg_function('datahub.post_plaid_transaction', [account_id, plaid_transaction_id, plaid_category_id, category, subcategory, amount, date_, pending, transaction], False)
        if transaction_insert_status:
            continue
        else:
            logging.error("Transaction with transaction_id %d did not insert", plaid_transaction_id)

def remove_transactions(transactions):
    print(transactions)
    try:
        for transaction in transactions:
            print('Removing Transaction')
            status, removed = call_pg_function('datahub.remove_transactions', [transaction], False)
    except:
        print('No Transactions to Remove')

def create_member(req_body):
    first_name = req_body['first_name'].title()
    last_name = req_body['last_name'].title()
    dob = req_body['birth_date']
    #age = calculate_age(dob)
    email = req_body['email_address'].lower()
    zipcode = req_body['postal_code']
    glorifi_login_id = req_body['glorifi_login_id']
    created_by = 'MEMBER_API'
    
    try:
        phone_number = str(req_body['phone_number'])
    except:
        phone_number = None
    try:
        preferred_name = req_body['preferred_name'].title()
    except:
        preferred_name = None
    try:
        address_line_1 = req_body['address_line_1']
        address_city = req_body['address_city'].title()
        address_state = req_body['address_state'].upper()
        address_country_code = req_body['address_country_code']
    except:
        address_line_1 = None
        address_city = None
        address_state = None
        address_country_code = None
    try:
        address_line_2 = req_body['address_line_2']
    except:
        address_line_2 = None

    

    cursor, conn = return_connection()
    cursor.execute("""INSERT INTO datahub.party(party_created_by, party_updated_by, party_first_name, party_last_name, party_dob,
        glorifi_login_id, party_email, party_zip) 
                    VALUES (%s,%s,%s,%s,%s::date,%s, %s, %s) 
                    RETURNING party_id""",
                    (created_by, created_by, first_name, last_name, dob, glorifi_login_id, email, zipcode))
    party_id = cursor.fetchone()
    party_id = int(party_id['party_id'])
    cursor.execute("""INSERT INTO datahub.member(member_created_by, member_updated_by, glorifi_login_id, party_id) 
                    VALUES (%s, %s, %s, %s) 
                    RETURNING member_id""", (created_by, created_by, glorifi_login_id, party_id))
    output = cursor.fetchone()

    if address_line_1 is not None:
        sql_statement = """INSERT INTO datahub.address(addr_address_line1, addr_city, 
        addr_state, addr_country, addr_postal_code)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING addr_id"""
        query_tuple = [address_line_1, address_city, address_state, address_country_code, zipcode]
        
        if address_line_2 is not None:
            sql_statement = sql_statement.split(')')[0] + ", addr_address_line2)" + sql_statement.split(')')[1] + ', %s)' + sql_statement.split(')')[2]
            query_tuple.append(address_line_2)

        query_tuple = tuple(query_tuple)
        cursor.execute(sql_statement, query_tuple)

        address_id = cursor.fetchone()
        address_id = int(address_id['addr_id'])
        end_date = "9999-12-31"

        cursor.execute("""INSERT INTO datahub.party_to_address(addr_id, party_id, end_date, is_preferred_addr)
        VALUES (%s, %s, %s, %s)""", (address_id, party_id, end_date, True))
    
    if phone_number is not None:
        phone_number = '+1' + str(phone_number).replace('-', '')
        cursor.execute("""SELECT * FROM datahub.comm_method_values
                            WHERE comm_method_value = %s""", (phone_number,))
        does_phone_exist = cursor.fetchone()
        if does_phone_exist == None:
            cursor.execute("""INSERT INTO datahub.comm_method_values(comm_method_value)
                VALUES(%s) RETURNING comm_method_id""", (phone_number,))
            comm_method_id = cursor.fetchone()
            comm_method_id = int(comm_method_id['comm_method_id'])
            cursor.execute("""INSERT INTO datahub.party_to_ani(party_id, ani_number, remember_ani)
                            VALUES (%s, %s, %s)""", (party_id, phone_number, 'Not Offered'))
        else:
            comm_method_id =  int(does_phone_exist['comm_method_id'])
        
        end_date = '9999-12-31'

        cursor.execute("""INSERT INTO datahub.party_to_comm_method(comm_method_id, party_id, comm_method_type, comm_pref_type, is_preferred_comm_method, valid_to_date)
        VALUES(%s, %s, %s, %s, %s, %s)""", (comm_method_id, party_id, 1, 0, True, end_date))


    cursor.close()
    conn.close()
    return output 

def refresh_accounts(accounts, item_id):
    """Table Columns
    item_id, plaid_account_id, name, mask, official_name, current_balance,
    available_balance, iso_currency_code, unofficial_currency_code, type,
    subtype, raw_json
    """
    item_id_arr = []
    account_id_arr = []
    subtype_arr = []
    status_arr = []
    account_name_arr = []
    mask_arr = []
    official_name_arr = []
    current_bal_arr = []
    available_bal_arr = []
    iso_curr_arr = []
    type_arr = []
    raw_json_arr = []
    try:
        for account in accounts:
            try:
                account_id_arr.append(account.get("account_id"))
                subtype_arr.append(str(account.get("subtype")))
                account_name_arr.append(str(account.get("name")))
                mask_arr.append(str(account.get("mask")))
                official_name_arr.append(str(account.get("official_name")))
                type_arr.append(str(account.get("type")))
                raw_json_arr.append(json.dumps(account.to_dict(), default=str))
                current_bal_arr.append(float(account.get(
                                            'balances', {}).get('current', None)))
                iso_curr_arr.append(str(account.get(
                                            'balances', {}).get('iso_currency_code', None)))
                available_bal_arr.append(float(account.get(
                                            'balances', {}).get('available', None)))
            except:
                continue
        status, _ = call_pg_function('ods_plaid.refresh_plaid_account', [item_id, account_id_arr, subtype_arr, account_name_arr, mask_arr, official_name_arr, current_bal_arr, available_bal_arr, iso_curr_arr, type_arr, raw_json_arr])
        if status:
            logging.info('Accounts Added')
        else:
            logging.info('Adding accounts failed')
    except Exception as e:
        logging.error("Exception occured while executing function: update_item_table_expiration_status\n" + traceback.format_exc())
