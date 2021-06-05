import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

def covid_19_20(conn: sqlite3):
    """

    """

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
    ax.yaxis.grid(True)
    plt.xticks(rotation=45)

    plt.show()

def avg_week_day(conn: sqlite3):

    df = pd.read_sql_query("SELECT CAST(AVG(accidents) AS INTEGER) as average, week_day_name, week_day_order FROM week_day GROUP BY week_day_name", conn)

    fig, ax = plt.subplots()

    df = df.set_index('week_day_name')
    df = df.sort_values('week_day_order')
    ax.set_title('Średnia liczba wypadków w zależności od dnia tygodnia w latach 2015 - 2020')
    ax.set_xlabel('Dni tygodnia')
    ax.set_ylabel('Liczba wypadków')
    ax.yaxis.grid(True)

    ax.bar(df.index, df['average'])

    plt.show()

def accidents_weekend_week(conn: sqlite3):
    """

    """

    df = pd.read_sql_query("SELECT week_day_name, accidents, week_day_order FROM week_day WHERE year=='2020'", conn)

    weekend_list = df[df['week_day_name']=='Piątek'].accidents.tolist() + \
              df[df['week_day_name']=='Sobota'].accidents.tolist() + \
              df[df['week_day_name']=='Niedziela'].accidents.tolist()

    weekend = sum(weekend_list)

    week = df['accidents'].sum() - weekend

    fig, ax = plt.subplots()
    ax.pie([weekend, week], labels=['Weekend(Pt, Sb, Nd)','Dni tygodnia(Pn, Wt, Śr, Czw)'], autopct=absoulte_relative_autopct([weekend, week]), startangle=90)
    ax.set_title('Porównanie liczby wypadków w weekendy i dni robocze, 2020')

    plt.show()

def killed_weekend_week(conn: sqlite3):
    """

    """

    df = pd.read_sql_query("SELECT week_day_name, killed, week_day_order FROM week_day WHERE year=='2020'", conn)

    weekend_list = df[df['week_day_name']=='Piątek'].killed.tolist() + \
              df[df['week_day_name']=='Sobota'].killed.tolist() + \
              df[df['week_day_name']=='Niedziela'].killed.tolist()

    weekend = sum(weekend_list)

    week = df['killed'].sum() - weekend

    fig, ax = plt.subplots()
    ax.pie([weekend, week], labels=['Weekend(Pt, Sb, Nd)','Dni tygodnia(Pn, Wt, Śr, Czw)'], autopct=absoulte_relative_autopct([weekend, week]), startangle=90)
    ax.set_title('Porównanie liczby ofiar w weekendy i dni robocze, 2020')

    plt.show()

def absoulte_relative_autopct(values):
    def calc(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}% ({v:d})'.format(p=pct,v=val)
    return calc
