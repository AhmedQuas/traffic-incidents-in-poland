import requests
from helpers.dataset_urls import *
from .csv_parser import parse_csv

def download_all():
    """

    """
    for key, value in dataset_driver_age.items():
        download_dataset(value[0], value[1], key)

def download_dataset(dataset_url: str, offset: int, dataset_year: int):
    """

    """
    
    response = requests.get(dataset_url)

    if response.status_code == 200:

        response_dict = response.json()
        title = response_dict['data']['attributes']['title']
        format = response_dict['data']['attributes']['format']
        url = response_dict['data']['attributes']['download_url']
        
        file = requests.get(url, allow_redirects=True)
        open('./dataset/tmp.csv','wb').write(file.content)

        if format == 'csv':
            parsed_csv = parse_csv('./dataset/tmp.csv', offset, dataset_year)
        else:
            print('Unsupported file format:', format)

    else:
        print('URL not found')
    
    print(parsed_csv)
