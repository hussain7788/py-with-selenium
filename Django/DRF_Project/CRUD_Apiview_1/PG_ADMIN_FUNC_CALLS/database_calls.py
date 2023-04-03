import psycopg2
from psycopg2.extras import RealDictCursor
import logging
from DRF_Project.settings import HOST, NAME, USER, PASSWORD, PORT

########### we need Valid DNS name (Host name) to connect psycopg2 database

def return_connection():
    conn = psycopg2.connect(host=HOST, database= NAME, user= USER, port= PORT, password= PASSWORD, cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    conn.set_session(autocommit=True)
    print("Database Connection Successfull")
    conn.set_session(autocommit=True)
    print("cursor and conn", cursor, conn)
    return cursor, conn
    # except:
    #     logging.error("Database Connection Failed")

def call_pg_func(pg_func, pg_params, fetch_all= True):
    output = None
    cursor , conn = return_connection()

    cursor.callproc(pg_func, pg_params)
    if fetch_all:
        output = cursor.fetchall()
    else:
        output = cursor.fetchone()
    cursor.close()
    conn.close()
    print("Connection Closed")
    # except:
    #     logging.error("Calling PG function failed")
    # finally:
    return output


def get_pg_func():
    data = call_pg_func('public.get_crud_table', [])
    print("data::", data)


# print(get_pg_func())



