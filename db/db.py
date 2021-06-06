import sqlite3
from sqlite3 import Error

def create_connection(db_file:str):
    """
    Create connection with SQLite db stored in specified path
    """

    conn = None

    try:
        conn = sqlite3.connect(db_file)

    except Error as e:
        print(e)

    return conn

def create_table(conn:sqlite3, sql_commnad:str):
    """
    Run given command that create table in db
    """
    
    try:
        c = conn.cursor()
        c.execute(sql_commnad)

    except Error as e:
        print(e)

def insert_data(conn:sqlite3, sql_command:str, data:tuple):
    """
    Insert given data to specified table
    """

    try:
        c = conn.cursor()
        c.execute(sql_command, data)
        conn.commit()

    except Error as e:
        print(e)