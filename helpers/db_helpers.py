import pandas as pd

def get_month_order_number(month):

    month_mapper = {
        'Styczeń': 1,
        'Luty': 2,
        'Marzec': 3,
        'Kwiecień': 4,
        'Maj': 5,
        'Czerwiec': 6,
        'Lipiec': 7,
        'Sierpień': 8,
        'Wrzesień': 9,
        'Październik': 10,
        'Listopad': 11,
        'Grudzień': 12
    }

    return month_mapper[month]

def get_day_order_number(day):

    day_mapper = {
        'Poniedziałek': 1,
        'Wtorek': 2,
        'Środa': 3,
        'Czwartek': 4,
        'Piątek': 5,
        'Sobota': 6,
        'Niedziela': 7
    }

    return day_mapper[day]