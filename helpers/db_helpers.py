import pandas as pd

# File contains function that map string to int value that is stored in db

def get_driver_age_order(age):

    driver_age_mapper = {
        '0-6': 1,
        '7-14': 2,
        '15-17': 3,
        '18-24': 4,
        '25-39': 5,
        '40-59': 6,
        '60 plus': 7,
        'b/d': 8
    }

    return driver_age_mapper[age]


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

def get_hour_order_number(hour):

    hour_mapper = {
        '00:00-00:59': 1,
        '01:00-01:59': 2,
        '02:00-02:59': 3,
        '03:00-03:59': 4,
        '04:00-04:59': 5,
        '05:00-05:59': 6,
        '06:00:06:59': 7,
        '07:00:07:59': 8,
        '08:00-08:59': 9,
        '09:00-09:59': 10,
        '10:00-10:59': 11,
        '11:00-11:59': 12,
        '12:00-12:59': 13,
        '13:00-13:59': 14,
        '14:00-14:59': 15,
        '15:00-15:59': 16,
        '16:00-16:59': 17,
        '17:00-17:59': 18,
        '18:00-18:59': 19,
        '19:00-19:59': 20,
        '20:00-20:59': 21,
        '21:00-21:59': 22,
        '22:00-22:59': 23,
        '23:00-23:59': 24,
    }

    return hour_mapper[hour]

def get_place_characteristic_number(place_characteristics):

    place_characteristic_mapper = {
        'Chodnik, droga dla pieszych': 1,
        'Droga, pas ruchu, śluza dla rowerów': 2,
        'Jezdnia': 3,
        'Most, wiadukt, łącznica, tunel': 4,
        'Parking, plac, MOP': 5,
        'Pas dzielący jezdnie': 6,
        'Pobocze': 7,
        'Przejazd dla rowerzystów': 8,
        'Przejazd kolejowy niestrzeżony': 9,
        'Przejazd kolejowy strzeżony': 10,
        'Przejazd tramwajowy, torowisko tramwajowe': 11,
        'Przejście dla pieszych': 12,
        'Przewiązka na drodze dwujezdniowej': 13,
        'Przystanek komunikacji publicznej': 14,
        'Roboty drogowe, oznakowanie tymczasowe': 15,
        'Skarpa, rów': 16,
        'Wjazd, wyjazd z posesji, pola': 17
    }

    return place_characteristic_mapper[place_characteristics]
