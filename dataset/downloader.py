import requests
import csv
from helpers.dataset_urls import *
from .csv_parser import parse_csv

def download_all():
    """

    """

    download_dataset(dataset_2020_urls['driver_age'])

def download_dataset(dataset_url: str):
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
            parse_csv()
        else:
            print('Unsupported file format:', format)

    else:
        print('URL not found')

