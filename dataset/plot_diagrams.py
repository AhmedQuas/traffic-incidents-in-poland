import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
from db import db
from helpers import plot_helpers

def plot_diagrams(db_file: str):
    """
    
    """

    conn = db.create_connection(db_file)

    pd.options.mode.chained_assignment = None  

    plot_month_covid_2019_2020_comparision(conn)

    conn.close()

def plot_month_covid_2019_2020_comparision(conn: sqlite3):
    
    df = pd.read_sql_query("SELECT year, month, accidents FROM months WHERE year IN('2020', '2019')", conn)

    fig, ax = plt.subplots()
    
    df_2019 = df[df['year']==2019]
    df_2020 = df[df['year']==2020]

    df_2019['monuth_number'] = plot_helpers.get_month_number(df_2019['month'])
    df_2019 = df_2019.sort_values('monuth_number')

    df_2020['monuth_number'] = plot_helpers.get_month_number(df_2020['month'])
    df_2020 = df_2020.sort_values('monuth_number')
    
    ax.bar(df_2019['month'], df_2019['accidents'], color='none', edgecolor = 'r')
    ax.bar(df_2020['month'], df_2020['accidents'], color='b', alpha=0.7 ,edgecolor = 'b')
    ax.set_title('Powrównanie liczby wypadków w latach 2019 i 2020')
    ax.set_xlabel('Miesiące')
    ax.set_ylabel('Liczba wypadków')
    ax.set_xticklabels(df_2019['month'], rotation=45)
    ax.legend(['2019', '2020'])

    plt.show()
