import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
from db import db

def plot_diagrams(db_file: str):
    """
    
    """

    conn = db.create_connection(db_file)

    pd.options.mode.chained_assignment = None  

    plot_month_covid_2019_2020_comparision(conn)

    conn.close()

def plot_month_covid_2019_2020_comparision(conn: sqlite3):
    
    df = pd.read_sql_query("SELECT year, month_name, accidents, month_id FROM months WHERE year IN('2020', '2019')", conn)

    fig, ax = plt.subplots()
    
    df_2019 = df[df['year']==2019].set_index('month_name')
    df_2020 = df[df['year']==2020].set_index('month_name')

    df_2019 = df_2019.sort_values('month_id')

    df_2020 = df_2020.sort_values('month_id')
    
    ax.bar(df_2019.index, df_2019['accidents'], color='none', edgecolor = 'r')
    ax.bar(df_2020.index, df_2020['accidents'], color='b', alpha=0.7 ,edgecolor = 'b')
    ax.set_title('Powrównanie liczby wypadków w latach 2019 i 2020')
    ax.set_xlabel('Miesiące')
    ax.set_ylabel('Liczba wypadków')
    ax.legend(['2019', '2020'])

    plt.xticks(rotation=45)

    plt.show()
