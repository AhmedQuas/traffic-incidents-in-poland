import requests
from helpers.dataset_urls import *
from .csv_parser import *

def download_all():
    """

    """
    for key, value in dataset_driver_age.items():
        download_dataset(value[0], value[1], key)
    
    print("===================================")

    for key, value in dataset_week_day.items():
        download_dataset(value[0], value[1], key)

def download_dataset(dataset_url: str, offset: int, dataset_year: str):
    """

    """
    driver_age_keywords = ['wiek kierującego', 'Wiek sprawcy kierującego', 'wiek sprawcy kierującego']
    week_day_keywords = ['podział na dni','dni tygodnia','']

    response = requests.get(dataset_url)

    if response.status_code == 200:

        response_dict = response.json()
        title = response_dict['data']['attributes']['title']
        format = response_dict['data']['attributes']['format']
        url = response_dict['data']['attributes']['download_url']
        
        file = requests.get(url, allow_redirects=True)
        open('./dataset/tmp.csv','wb').write(file.content)

        if format == 'csv':
            if [el for el in driver_age_keywords if(el in title)]:
                parsed_csv = parse_csv_driver_age('./dataset/tmp.csv', offset, dataset_year)
            elif [el for el in week_day_keywords if(el in title)]:
                parsed_csv = parse_csv_week_day('./dataset/tmp.csv', offset, dataset_year)
            else:
                print('Nieobslugiwany tytul danych')
        else:
            print('Unsupported file format:', format)

    else:
        print('URL not found')
    
    print(parsed_csv)
