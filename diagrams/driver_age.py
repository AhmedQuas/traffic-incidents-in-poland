import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

def accidents(conn: sqlite3):

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

    p1.set_title('Powrównanie liczby wypadków w zależności od grupy wiekowej')
    p1.set_xlabel('Grupy wiekowe')
    p1.set_ylabel('Liczba wypadków')
    
    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.show()
