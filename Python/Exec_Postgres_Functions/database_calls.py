import logging
import traceback
from gloripy.utils.http_response_handler import NotFound

import psycopg2
import logging
from psycopg2.extras import RealDictCursor, DictCursor
import config_managemnt.config as settings
import os


# PostGRES credentials
POSTGRESS_DB_PASSWORD = os.getenv("POSTGRESS_DB_PASSWORD")
POSTGRESS_DB_NAME = os.getenv("POSTGRESS_DB_NAME")
POSTGRESS_DB_PORT = os.getenv("POSTGRESS_DB_PORT")
POSTGRESS_HOST = os.getenv("POSTGRESS_HOST")
POSTGRESS_USER = os.getenv("POSTGRESS_USER")

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
    output = None
    logging.info("Started executing postgres function: {0}".format(pg_fn_name))
    try:
        cursor, conn = return_connection()
        cursor.callproc(pg_fn_name, param_list)
        if fetchall:
            output = cursor.fetchall()
        else:
            output = cursor.fetchone()
        cursor.close()
        conn.close()
        logging.info('Database Connection Closed')
    except Exception as e:
        logging.error("Exception occured while executing postgres function:" + traceback.format_exc())
        logging.error('datahub.post_plaid_auth_accounts Failed.')
        raise NotFound("datahub.post_plaid_auth_accounts Failed")
    
    logging.info("Ended executing postgres function: {0}".format(pg_fn_name))
    return output