import matplotlib.pyplot as plt
from numpy import msort
import pandas as pd
import sqlite3
from helpers import db_helpers

def avg_hour(conn: sqlite3):
    """

    """

    df = pd.read_sql_query("SELECT CAST(AVG(accidents) AS INTEGER) as average, hour_name, hour_order FROM hours GROUP BY hour_name", conn)

    fig, ax = plt.subplots()

    df = df.set_index('hour_name')
    df = df.sort_values('hour_order')
    ax.set_title('Średnia liczba wypadków w zależności od godziny wypadku w latach 2015 - 2020')
    ax.set_xlabel('Godzina zdarzenia')
    ax.set_ylabel('Liczba wypadków')
    ax.yaxis.grid(True)

    ax.bar(df.index, df['average'])
    plt.xticks(rotation=45)

    plt.show()

def avg_hour_with_2020(conn: sqlite3):
    """

    """

    df_avg = pd.read_sql_query("SELECT CAST(AVG(accidents) AS INTEGER) as average, hour_name, hour_order FROM hours GROUP BY hour_name", conn)
    df_2020 = pd.read_sql_query("SELECT accidents, hour_name, hour_order FROM hours WHERE year=='2020'", conn)


    fig, ax = plt.subplots()

    df_avg = df_avg.set_index('hour_name')
    df_avg = df_avg.sort_values('hour_order')

    df_2020 = df_2020.set_index('hour_name')
    df_2020 = df_2020.sort_values('hour_order')


    ax.set_title('Porównanie danych z 2020 ze średnią z lat 2015-2020 - podział ze względu na godzinę zdarzenia')
    ax.set_xlabel('Godzina zdarzenia')
    ax.set_ylabel('Liczba wypadków')
    ax.yaxis.grid(True)

    ax.bar(df_avg.index, df_avg['average'], color='none', edgecolor = 'r')
    ax.bar(df_2020.index, df_2020['accidents'], color='b', alpha=0.7 ,edgecolor = 'b')
    ax.legend(['Średnia w latach 2015-2020','2020'])

    plt.xticks(rotation=45)

    plt.show()

def rush_hours(conn: sqlite3):
    """

    """

    df = pd.read_sql_query("SELECT hour_name, accidents, hour_order FROM hours WHERE year=='2020'", conn)

    morning_rush_hours_list = df[df['hour_name']=='07:00:07:59'].accidents.tolist() + \
                              df[df['hour_name']=='08:00-08:59'].accidents.tolist()

    afternoon_rush_hours_list = df[df['hour_name']=='15:00-15:59'].accidents.tolist() + \
                                df[df['hour_name']=='16:00-16:59'].accidents.tolist()

    morning_rush_hours = sum(morning_rush_hours_list)
    afternoon_rush_hours = sum(afternoon_rush_hours_list)


    fig, ax = plt.subplots()

    ax.bar(['Poranne godziny szczytu(7-9)','Popołudniowe godziny szczytu(15-17)'], [morning_rush_hours, afternoon_rush_hours])
    ax.set_title('Porównanie liczby wypadków w zależności od pory godzin szczytu, 2020')
    ax.yaxis.grid(True)

    plt.show()

def time_day(conn: sqlite3):
    """

    """

    df = pd.read_sql_query("SELECT hour_name, accidents, hour_order FROM hours WHERE year=='2020'", conn)

    df = df.set_index('hour_name')
    df.sort_values('hour_order')

    morning_list = df[db_helpers.get_hour_order_number('04:00-04:59')-1:db_helpers.get_hour_order_number('11:00-11:59')].accidents.tolist()
    afternoon_list = df[db_helpers.get_hour_order_number('12:00-12:59')-1:db_helpers.get_hour_order_number('19:00-19:59')].accidents.tolist()

    morning = sum(morning_list)
    afternoon = sum(afternoon_list)

    evening = df['accidents'].sum() - morning - afternoon

    x_axis = [morning, afternoon, evening]

    fig1, ax1 = plt.subplots()
    ax1.pie(x_axis, labels=['Godziny poranne(4-12)','Godziny popołudniowe(12-20)','Godziny nocne(20-4)'], autopct=absoulte_relative_autopct(x_axis), startangle=180)
    ax1.axis('equal')

    ax1.set_title('Liczba wypadków w zależności od pory dnia, 2020')

    plt.show()

def absoulte_relative_autopct(values):
    def calc(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}% ({v:d})'.format(p=pct,v=val)
    return calc
