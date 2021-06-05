import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

def covid_19_20(conn: sqlite3):

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
