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
    
    """

    conn = db.create_connection(db_file)

    pd.options.mode.chained_assignment = None  

    #driver_age.accidents(conn)
    #driver_age.pie_collisions(conn)
    #driver_age.pie_accidents(conn)
    #driver_age.pie_killed(conn)
    #driver_age.pie_injured(conn)

    #week_day.covid_19_20(conn)
    #week_day.avg_week_day(conn)
    #week_day.accidents_weekend_week(conn)
    #week_day.killed_weekend_week(conn)

    #place_characteristics.active_unguarded_level_crossing_accidents(conn)
    #place_characteristics.active_crossing_level_year_accidents(conn)

    #hour.avg_hour(conn)
    #hour.rush_hours(conn)
    #hour.time_day(conn)

    #month.covid_19_20(conn)
    #month.avg_month(conn)

    conn.close()
