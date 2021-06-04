import requests
from helpers.dataset_urls import *
from .csv_parser import *
from .excel_parser import *

def download_all():
    """

    """

    driver_age = []
    week_day = []
    months = []
    hours = []
    place_characteristics = []

    print('Download status:')

    for year, [url, offset] in dataset_driver_age.items():

        dataset = download_dataset(url, offset, year)
        if year == '2020':
            driver_age.append(dataset)
        else:
            driver_age.append(dataset[1:])

    print(" - Driver age - OK!")

    for year, [url, offset] in dataset_week_day.items():

        dataset = download_dataset(url, offset, year)
        if year == '2020':
            week_day.append(dataset)
        else:
            week_day.append(dataset[1:])

    print(" - Days of weeek - OK!")

    for year, [url, offset] in dataset_months.items():

        dataset = download_dataset(url, offset, year)
        if year == '2020':
            months.append(dataset)
        else:
            months.append(dataset[1:])

    print(" - Months - OK!")

    for year, [url, offset] in dataset_hours.items():

        dataset = download_dataset(url, offset, year)
        if year == '2020':
            hours.append(dataset)
        else:
            hours.append(dataset[1:])

    print(" - Hours - OK!")

    for year, [url, offset] in dataset_place_characteristics.items():

        dataset = download_dataset(url, offset, year)
        if year == '2020':
            place_characteristics.append(dataset)
        else:
            place_characteristics.append(dataset[1:])

    print("Download stage complete.")

    return{
        'driver_age': driver_age,
        'week_day': week_day,
        'months': months,
        'hours': hours,
        'place_characteristics': place_characteristics
    }

def download_dataset(dataset_url: str, offset: int, dataset_year: str):
    """

    """
    driver_age_keywords = ['wiek kierującego', 'Wiek sprawcy kierującego', 'wiek sprawcy kierującego']
    week_day_keywords = ['podział na dni', 'dni tygodnia']
    months_keywords = ['podział na miesiące', 'podziale na miesiące', '- miesiące']
    hours_keywords = ['podział na godziny', 'podziale na godziny', '- godziny']
    place_characteristics_keywords = ['charakterystyka miejsca', 'Charakterystyka miejsca']
    place_characteristics_xlsx_keywords = 'w 2019 r. - dane zbiorcze'
    place_characteristics_xls_keywords = '2018 r. - charakterystyka miejsca'

    response = requests.get(dataset_url)

    if response.status_code == 200:

        response_dict = response.json()
        tmp_filename = './dataset/tmp'

        title = response_dict['data']['attributes']['title']
        format = response_dict['data']['attributes']['format']
        url = response_dict['data']['attributes']['download_url']
        
        file = requests.get(url, allow_redirects=True)

        if format == 'csv':

            tmp_filename = tmp_filename+'.csv'
            open(tmp_filename,'wb').write(file.content)

            if [el for el in driver_age_keywords if(el in title)]:
                parsed_data = parse_csv_driver_age(tmp_filename, offset, dataset_year)

            elif [el for el in week_day_keywords if(el in title)]:
                parsed_data = parse_csv_week_day(tmp_filename, offset, dataset_year)

            elif [el for el in months_keywords if(el in title)]:
                parsed_data = parse_csv_month(tmp_filename, offset, dataset_year)

            elif [el for el in hours_keywords if(el in title)]:
                parsed_data = parse_csv_hours(tmp_filename, offset, dataset_year)

            elif [el for el in place_characteristics_keywords if(el in title)]:
                parsed_data = parse_csv_place_characteristics(tmp_filename, offset, dataset_year)

            else:
                print('Unsupported dataset title:', title)

        elif format =='xlsx':

            tmp_filename = tmp_filename+'.xlsx'
            open(tmp_filename,'wb').write(file.content)

            if place_characteristics_xlsx_keywords in title:
                parsed_data = parse_xlsx_place_characteristics(tmp_filename, offset, dataset_year)

            else:
                print('Unsupported dataset title:', title)

        elif format =='xls':

            tmp_filename = tmp_filename+'.xls'
            open(tmp_filename,'wb').write(file.content)

            if place_characteristics_xls_keywords in title:
                parsed_data = parse_xls_place_characteristics(tmp_filename, offset, dataset_year)

            else:
                print('Unsupported dataset title:', title)

        else:
            print('Unsupported file format:', format)

    else:
        print('URL not found')
    
    #Add year timestamp
    for line in parsed_data:
        line.append(dataset_year)

    return parsed_data
