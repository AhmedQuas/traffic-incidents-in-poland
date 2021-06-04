import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
from db import db

def plot_diagrams(db_file: str):
    """
    
    """

    conn = db.create_connection(db_file)

    pd.options.mode.chained_assignment = None  

    #plot_month_covid_2019_2020_comparision(conn)
    #plot_week_day_covid_2019_2020_comparision(conn)
    accidents_by_driver_age(conn)
    accidents_by_driver_age_v2(conn)

    conn.close()

def plot_month_covid_2019_2020_comparision(conn: sqlite3):

    df = pd.read_sql_query("SELECT year, month_name, accidents, month_order FROM months WHERE year IN('2020', '2019')", conn)

    fig, ax = plt.subplots()

    df_2019 = df[df['year']==2019].set_index('month_name')
    df_2020 = df[df['year']==2020].set_index('month_name')

    df_2019 = df_2019.sort_values('month_order')

    df_2020 = df_2020.sort_values('month_order')

    ax.bar(df_2019.index, df_2019['accidents'], color='none', edgecolor = 'r')
    ax.bar(df_2020.index, df_2020['accidents'], color='b', alpha=0.7 ,edgecolor = 'b')
    ax.set_title('Powrównanie liczby wypadków w latach 2019 i 2020')
    ax.set_xlabel('Miesiące')
    ax.set_ylabel('Liczba wypadków')
    ax.legend(['2019', '2020'])
    plt.xticks(rotation=45)

    plt.show()

def plot_week_day_covid_2019_2020_comparision(conn: sqlite3):

    df = pd.read_sql_query("SELECT year, week_day_name, accidents, week_day_order FROM week_day WHERE year IN('2020', '2019')", conn)

    fig, ax = plt.subplots()

    df_2019 = df[df['year']==2019].set_index('week_day_name')
    df_2020 = df[df['year']==2020].set_index('week_day_name')

    df_2019 = df_2019.sort_values('week_day_order')

    df_2020 = df_2020.sort_values('week_day_order')

    ax.bar(df_2019.index, df_2019['accidents'], color='none', edgecolor = 'r')
    ax.bar(df_2020.index, df_2020['accidents'], color='b', alpha=0.7 ,edgecolor = 'b')
    ax.set_title('Powrównanie liczby wypadków w latach 2019 i 2020')
    ax.set_xlabel('Dni tygodnia')
    ax.set_ylabel('Liczba wypadków')
    ax.legend(['2019', '2020'])
    plt.xticks(rotation=45)

    plt.show()

def accidents_by_driver_age(conn: sqlite3):

    df = pd.read_sql_query("SELECT year, age_name, accidents, age_order FROM driver_age", conn)

    fig, ax = plt.subplots()

    df.set_index('year')
    df = df.sort_values(['year', 'age_order'], ascending=[True, True])

    groups = []

    for i in range(1,9):
        temp = df[df['age_order']==i]
        groups.append(temp['accidents'].values.tolist())

    group_labels = ['0-6','7-14','15-17','18-24','25-39','40-59','60+','b/d']

    df = pd.DataFrame(groups, index=group_labels).T

    df.index = [2015, 2016, 2017, 2018, 2019, 2020]

    p1 = pd.concat([df], axis=1).plot.bar(grid=True)

    ax.set_title('Powrównanie liczby wypadków w zależności od grupy wiekowej')
    ax.set_xlabel('Grupy wiekowe')
    ax.set_ylabel('Liczba wypadków')
    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.show()


def accidents_by_driver_age_v2(conn: sqlite3):

    df = pd.read_sql_query("SELECT year, age_name, accidents, age_order FROM driver_age", conn)

    fig, ax = plt.subplots()

    df.set_index('year')
    df = df.sort_values(['year', 'age_order'], ascending=[True, True])

    groups = []

    for i in [2015, 2016, 2017, 2018, 2019, 2020]:
        temp = df[df['year']==i]
        groups.append(temp['accidents'].values.tolist())

    group_labels = [2015, 2016, 2017, 2018, 2019, 2020]

    df = pd.DataFrame(groups, index=group_labels).T

    df.index = ['0-6','7-14','15-17','18-24','25-39','40-59','60+','b/d']

    pd.concat([df], axis=1).plot.bar(grid=True)

    plt.show()