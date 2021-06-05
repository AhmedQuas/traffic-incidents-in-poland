import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
from .plot_diagrams import *

def accidents(conn: sqlite3):
    """

    """

    df = pd.read_sql_query("SELECT year, age_name, accidents, age_order FROM driver_age", conn)

    #fig, ax = plt.subplots()

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

    p1.set_title('Powrównanie liczby wypadków w zależności od grupy wiekowej - sprawcy')
    p1.set_xlabel('Grupy wiekowe')
    p1.set_ylabel('Liczba wypadków')

    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.show()

def pie_collisions(conn: sqlite3):
    """

    """

    df = pd.read_sql_query("SELECT age_name, collisions, age_order FROM driver_age WHERE year=='2020' AND NOT age_order IN (1,2,3)", conn)

    df = df.sort_values(['age_order'])
    df = df.set_index('age_name')

    fig1, ax1 = plt.subplots()
    ax1.pie(df['collisions'], labels=df.index.tolist(), autopct=absoulte_relative_autopct(df['collisions']), startangle=180)
    ax1.axis('equal')

    ax1.set_title('Liczba kolizji w zależności od grupy wiekowej - sprawcy')

    plt.show()

def pie_accidents(conn: sqlite3):
    """

    """

    df = pd.read_sql_query("SELECT age_name, accidents, age_order FROM driver_age WHERE year=='2020' AND NOT age_order IN (1,2,3)", conn)

    df = df.sort_values(['age_order'])
    df = df.set_index('age_name')

    fig1, ax1 = plt.subplots()
    ax1.pie(df['accidents'], labels=df.index.tolist(), autopct=absoulte_relative_autopct(df['accidents']), startangle=180)
    ax1.axis('equal')

    ax1.set_title('Liczba wypadków w zależności od grupy wiekowej - sprawcy')

    plt.show()

def pie_killed(conn: sqlite3):
    """

    """

    df = pd.read_sql_query("SELECT age_name, killed, age_order FROM driver_age WHERE year=='2020' AND NOT age_order IN (1,2,3)", conn)

    df = df.sort_values(['age_order'])
    df = df.set_index('age_name')

    fig1, ax1 = plt.subplots()
    ax1.pie(df['killed'], labels=df.index.tolist(), pctdistance=0.7, autopct=absoulte_relative_autopct(df['killed']), startangle=180)
    ax1.axis('equal')

    ax1.set_title('Liczba ofiar śmiertelnych w zależności od grupy wiekowej do jakiej należy sprawca')

    plt.show()

def pie_injured(conn: sqlite3):
    """

    """

    df = pd.read_sql_query("SELECT age_name, injured, age_order FROM driver_age WHERE year=='2020' AND NOT age_order IN (1,2,3)", conn)

    df = df.sort_values(['age_order'])
    df = df.set_index('age_name')

    fig1, ax1 = plt.subplots()
    ax1.pie(df['injured'], labels=df.index.tolist(), pctdistance=0.7, autopct=absoulte_relative_autopct(df['injured']), startangle=180)
    ax1.axis('equal')

    ax1.set_title('Liczba rannych w zależności od grupy wiekowej do jakiej należy sprawca')

    plt.show()

def absoulte_relative_autopct(values):
    def calc(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}% ({v:d})'.format(p=pct,v=val)
    return calc
