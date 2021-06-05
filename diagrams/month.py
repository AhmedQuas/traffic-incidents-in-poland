import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

def covid_19_20(conn: sqlite3):

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
    ax.yaxis.grid(True)
    ax.legend(['2019', '2020'])
    plt.xticks(rotation=45)

    plt.show()

def avg_month(conn: sqlite3):


    df = pd.read_sql_query("SELECT CAST(AVG(accidents) AS INTEGER) as average, month_name, month_order FROM months GROUP BY month_name", conn)

    fig, ax = plt.subplots()

    df = df.set_index('month_name')
    df = df.sort_values('month_order')
    ax.set_title('Średnia liczba wypadków w latach 2015 - 2020 - podział na miesiące')
    ax.set_ylabel('Liczba wypadków')
    ax.yaxis.grid(True)

    ax.bar(df.index, df['average'])
    plt.xticks(rotation=45)

    plt.show()