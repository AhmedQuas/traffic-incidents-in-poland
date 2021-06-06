import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
from db import db
from . import driver_age
from . import hour
from . import month
from . import place_characteristics
from . import trends
from . import week_day

def plot_diagrams(db_file: str):
    """
    It is responsible for plotting diagrams, all function that plot diagrams are registered below
    """

    conn = db.create_connection(db_file)

    pd.options.mode.chained_assignment = None  

    print('Plotting status:')

    driver_age.accidents(conn)
    driver_age.pie_collisions(conn)
    driver_age.pie_accidents(conn)
    driver_age.pie_killed(conn)
    driver_age.pie_injured(conn)
    print(' - Driver age - OK!')

    week_day.covid_19_20(conn)
    week_day.avg_week_day(conn)
    week_day.accidents_weekend_week(conn)
    week_day.killed_weekend_week(conn)
    week_day.avg_week_day_with_2020(conn)
    print(" - Days of weeek - OK!")

    place_characteristics.active_unguarded_level_crossing_accidents(conn)
    place_characteristics.active_crossing_level_year_accidents(conn)
    print(" - Place characteristics - OK!")

    hour.avg_hour(conn)
    hour.rush_hours(conn)
    hour.time_day(conn)
    hour.avg_hour_with_2020(conn)
    print(" - Hours - OK!")

    month.covid_19_20(conn)
    month.avg_month(conn)
    month.pie_month(conn)
    print(" - Months - OK!")

    trends.accidents_min_max_year(conn)
    trends.year_aggregation(conn)
    print(" - Trends - OK!")

    print("Plotting stage complete.")

    conn.close()
