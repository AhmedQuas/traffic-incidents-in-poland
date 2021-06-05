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

    #month.covid_19_20(conn)
    #week_day.covid_19_20(conn)
    driver_age.accidents(conn)

    conn.close()
