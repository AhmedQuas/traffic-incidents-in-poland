import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

def active_unguarded_level_crossing_accidents(conn: sqlite3):
    """

    """

    df = pd.read_sql_query("SELECT place_characteristic_name, accidents FROM place_characteristics WHERE year=='2020'", conn)

    fig, ax = plt.subplots()

    df_active = df[df['place_characteristic_name']=='Przejazd kolejowy strzeżony'].accidents.tolist()
    df_unguarder = df[df['place_characteristic_name']=='Przejazd kolejowy niestrzeżony'].accidents.tolist()

    ax.bar(['Przejazd kolejowy strzeżony','Przejazd kolejowy niestrzeżony'], [df_active[0], df_unguarder[0]])
    ax.set_title('Liczba wypadków w zależności od typu przejazdu kolejowego w 2020')
    ax.set_ylabel('Liczba wypadków')

    plt.show()

def active_crossing_level_year_accidents(conn: sqlite3):
    """

    """

    df = pd.read_sql_query("SELECT place_characteristic_name, year, accidents FROM place_characteristics WHERE "\
        "place_characteristic_name=='Przejazd kolejowy strzeżony'", conn)

    df = df.set_index('year')
    df = df.sort_values(['year'], ascending=[False])

    fig, ax = plt.subplots()

    max = df['accidents'].max()

    ax.barh(df.index, df['accidents'])
    ax.set_title('Liczba wypadków w na przejazdach kolejowych strzeżonych w latach 2016 - 2020')
    ax.set_xlabel('Liczba wypadków')
    plt.xticks(range(0,max+1))

    plt.show()
