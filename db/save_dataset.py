import sqlite3
from sqlite3 import Error
from typing import Dict
from . import db

def save_dataset_in_db(downloaded_data:Dict, db_file: str):

    conn = db.create_connection(db_file)

    print('Saving dataset into SQLite:')

    create_driver_age_table(conn, downloaded_data['driver_age'])
    create_week_day_table(conn, downloaded_data['week_day'])
    create_months_table(conn, downloaded_data['months'])
    create_hours_table(conn, downloaded_data['hours'])
    create_place_characteristics_table(conn, downloaded_data['place_characteristics'])

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

    #Make sure that text convention is consistent
    age_values = []

    for i in range(len(dataset[0])):
        age_values.append(dataset[0][i][0])

    for row in dataset:
        for i in range(len(row)):
            data_tuple=(age_values[i],
                    int(row[i][1].replace(' ','')),
                    int(row[i][2].replace(' ','')),
                    int(row[i][3].replace(' ','')),
                    int(row[i][4].replace(' ','')),
                    int(row[i][5].replace(' ','')))

            db.insert_data(conn, sql_insert_data, data_tuple)

    print(' - Driver age - OK!')

def create_week_day_table(conn:sqlite3, dataset:Dict):

    sql_create_week_day_table = """

    CREATE TABLE IF NOT EXISTS week_day(
        year integer,
        week_day text,
        accidents integer,
        killed integer,
        injured integer,
        collisions integer,
        PRIMARY KEY(year, week_day)
    )
    """

    db.create_table(conn, sql_create_week_day_table)

    sql_insert_data = """
    INSERT OR IGNORE INTO week_day(week_day, accidents, killed, injured, collisions, year)
    VALUES (?,?,?,?,?,?)
    """

    #Remove header
    dataset[0].pop(0)

    #Make sure that text convention is consistent
    weekday_values = []

    for i in range(len(dataset[0])):
        weekday_values.append(dataset[0][i][0])

    for row in dataset:
        for i in range(len(row)):
            data_tuple=(weekday_values[i],
                    int(row[i][1].replace(' ','')),
                    int(row[i][2].replace(' ','')),
                    int(row[i][3].replace(' ','')),
                    int(row[i][4].replace(' ','')),
                    int(row[i][5]))

            db.insert_data(conn, sql_insert_data, data_tuple)

    print(' - Days of weeek - OK!')

def create_months_table(conn:sqlite3, dataset:Dict):

    sql_create_months_table = """

    CREATE TABLE IF NOT EXISTS months(
        year integer,
        month text,
        accidents integer,
        killed integer,
        injured integer,
        collisions integer,
        PRIMARY KEY(year, month)
    )
    """

    db.create_table(conn, sql_create_months_table)

    sql_insert_data = """
    INSERT OR IGNORE INTO months(month, accidents, killed, injured, collisions, year)
    VALUES (?,?,?,?,?,?)
    """

    #Remove header
    dataset[0].pop(0)

    #Make sure that text convention is consistent
    month_values = []

    for i in range(len(dataset[0])):
        month_values.append(dataset[0][i][0])

    for row in dataset:
        for i in range(len(row)):
            data_tuple=(month_values[i],
                    int(row[i][1].replace(' ','')),
                    int(row[i][2].replace(' ','')),
                    int(row[i][3].replace(' ','')),
                    int(row[i][4].replace(' ','')),
                    int(row[i][5]))

            db.insert_data(conn, sql_insert_data, data_tuple)

    print(' - Months - OK!')

def create_hours_table(conn:sqlite3, dataset:Dict):

    sql_create_hours_table = """

    CREATE TABLE IF NOT EXISTS hours(
        year integer,
        hour text,
        accidents integer,
        killed integer,
        injured integer,
        collisions integer,
        PRIMARY KEY(year, hour)
    )
    """

    db.create_table(conn, sql_create_hours_table)

    sql_insert_data = """
    INSERT OR IGNORE INTO hours(hour, accidents, killed, injured, collisions, year)
    VALUES (?,?,?,?,?,?)
    """

    #Remove header
    dataset[0].pop(0)

    #Make sure that text convention is consistent
    hour_values = []

    for i in range(len(dataset[0])):
        hour_values.append(dataset[0][i][0])

    for row in dataset:
        for i in range(len(row)):
            data_tuple=(hour_values[i],
                    int(row[i][1].replace(' ','')),
                    int(row[i][2].replace(' ','')),
                    int(row[i][3].replace(' ','')),
                    int(row[i][4].replace(' ','')),
                    int(row[i][5]))

            db.insert_data(conn, sql_insert_data, data_tuple)

    print(' - Hours - OK!')

def create_place_characteristics_table(conn:sqlite3, dataset:Dict):

    sql_create_hours_table = """

    CREATE TABLE IF NOT EXISTS place_characteristics(
        year integer,
        place_characteristic text,
        accidents integer,
        killed integer,
        injured integer,
        collisions integer,
        PRIMARY KEY(year, place_characteristic)
    )
    """

    db.create_table(conn, sql_create_hours_table)

    sql_insert_data = """
    INSERT OR IGNORE INTO place_characteristics(place_characteristic, accidents, killed, injured, collisions, year)
    VALUES (?,?,?,?,?,?)
    """

    #Remove header
    dataset[0].pop(0)

    #Make sure that text convention is consistent
    place_characteristic_values = []

    for i in range(len(dataset[0])):
        place_characteristic_values.append(dataset[0][i][0])

    for row in dataset:
        for i in range(len(row)):

            if (row[i][5] == '2019'):
                data_tuple=(place_characteristic_values[i],
                        row[i][1],
                        row[i][2],
                        row[i][3],
                        row[i][4],
                        int(row[i][5]))

            else:
                data_tuple=(place_characteristic_values[i],
                        int(row[i][1].replace(' ','')),
                        int(row[i][2].replace(' ','')),
                        int(row[i][3].replace(' ','')),
                        int(row[i][4].replace(' ','')),
                        int(row[i][5]))

            db.insert_data(conn, sql_insert_data, data_tuple)

    print(' - Place characteristic - OK!')
