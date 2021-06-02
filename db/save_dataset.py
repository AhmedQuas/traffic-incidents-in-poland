import sqlite3
from sqlite3 import Error
from typing import Dict
from . import db

def save_dataset_in_db(downloaded_data:Dict, db_file):

    conn = db.create_connection(db_file)

    print('Saving dataset into SQLite:')

    create_driver_age_table(conn, downloaded_data['driver_age'])

    conn.close()

def create_driver_age_table(conn:sqlite3, dataset:Dict):

    sql_create_driver_age_table = """

    CREATE TABLE IF NOT EXISTS driver_age(
        year integer,
        age text,
        accidents integer,
        killed integer,
        injured integer,
        collisions integer,
        PRIMARY KEY(year, age)
    )
    """

    db.create_table(conn, sql_create_driver_age_table)

    sql_insert_data = """
    INSERT OR IGNORE INTO driver_age(age, accidents, killed, injured, collisions, year)
    VALUES (?,?,?,?,?,?)
    """

    #Remove header
    dataset[0].pop(0)

    for row in dataset:
        for data in row:
            data_tuple=(data[0],
                    int(data[1]),
                    int(data[2]),
                    int(data[3]),
                    int(data[4]),
                    int(data[5]))

            db.insert_data(conn, sql_insert_data, data_tuple)

    print(' - Driver age - OK!')