import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

def accidents_min_max_year(conn: sqlite3):
    """

    """

    df_min = pd.read_sql_query("SELECT MIN(accidents) AS min_accidents, month_name, month_order, year FROM months GROUP BY year", conn)
    df_max = pd.read_sql_query("SELECT MAX(accidents) AS max_accidents, month_name, month_order, year FROM months GROUP BY year", conn)

    df_min.set_index('year')
    df_min = df_min.sort_values(['year'])

    df_max.set_index('year')
    df_max = df_max.sort_values(['year'])

    groups = []

    groups.append(df_max['max_accidents'].values.tolist())

    groups.append(df_min['min_accidents'].values.tolist())

    group_labels = ['Miesiąc z minimalną liczba wypadków w danym roku','Miesiąc z maksmalną liczbą wypadków w danym roku']

    df = pd.DataFrame(groups, index=group_labels).T

    df.index = [2015, 2016, 2017, 2018, 2019, 2020]

    p1 = pd.concat([df], levels = ['stst','asd'],axis =1).plot.bar(grid=True)

    p1.set_title('Powrównanie maksymalnej i minimalnej liczby wypdaków w latach 2015 - 2020')
    p1.set_xlabel('Miesiące')
    p1.set_ylabel('Liczba wypadków')

    plt.xticks(rotation=45)

    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()

    fig1.patch.set_visible(False)
    ax1.axis('off')
    ax1.axis('tight')

    fig2.patch.set_visible(False)
    ax2.axis('off')
    ax2.axis('tight')

    max_table = df_max[['year','max_accidents','month_name']]
    max_table = max_table.sort_values('year', ascending=False)
    max_table = max_table.set_index('year')

    min_table = df_min[['year','min_accidents','month_name']]
    min_table = min_table.sort_values('year', ascending=False)
    min_table = min_table.set_index('year')


    ax1.table(colLabels=['Liczba wypadków','Miesiąc'], rowLabels=max_table.index, cellText=max_table.values)
    ax1.set_title('Miesiące z największą liczbą wypadków')
    fig1.tight_layout()

    ax2.table(colLabels=['Liczba wypadków','Miesiąc'], rowLabels=min_table.index, cellText=min_table.values)
    ax2.set_title('Miesiące z najmniejszą liczbą wypadków')
    fig2.tight_layout()

    plt.show()
