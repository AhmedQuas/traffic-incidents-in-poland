import pandas as pd

def get_month_number(months):

    month_numbers = []

    month_mapper = {
        'Styczeń':1,
        'Luty':2,
        'Marzec':3,
        'Kwiecień':4,
        'Maj': 5,
        'Czerwiec': 6,
        'Lipiec': 7,
        'Sierpień': 8,
        'Wrzesień': 9,
        'Październik': 10,
        'Listopad': 11,
        'Grudzień': 12
    }
    
    for month in months:
        month_numbers.append(month_mapper[month])

    return month_numbers