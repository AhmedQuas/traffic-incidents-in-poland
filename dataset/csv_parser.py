import csv
import re

def parse_csv_driver_age(path: str, line_offset: int, dataset_year: str):
    """

    """

    with open(path, encoding='cp1250') as file:
        csv_reader = csv.reader(file, delimiter=';')
        
        line_count = 0
        parsed_data = []

        for row in csv_reader:
            if line_count >= line_offset:
                row[0] = re.sub('^[0-9]: ','',row[0])
                parsed_data.append(row)
            
            line_count += 1

        # Remove blank row
        if dataset_year == "2017":
            del parsed_data[-1]

        # Remove Summary row
        del parsed_data[-1]

    return parsed_data

def parse_csv_week_day(path: str, line_offset: int, dataset_year: int):
    """

    """

    with open(path, encoding='cp1250') as file:
        csv_reader = csv.reader(file, delimiter=';')
        
        line_count = 0
        parsed_data = []

        for row in csv_reader:
            if line_count >= line_offset:
                parsed_data.append(row)
            
            line_count += 1

        # Remove blank row
        if dataset_year == "2017":
            del parsed_data[-1]

        # Remove weird whitespaces
        if dataset_year == "2018":
            for i in range(1,len(parsed_data)):
                days = re.findall('[A-ZĄĆĘŁŃÓŚŻŹa-ząćęłńóśżź]', parsed_data[i][0])
                parsed_data[i][0] = ''.join(days)

        # Remove Summary row
        del parsed_data[-1]

    return parsed_data

def parse_csv_month(path: str, line_offset: int, dataset_year: int):
    """

    """

    with open(path, encoding='cp1250') as file:
        csv_reader = csv.reader(file, delimiter=';')
        
        line_count = 0
        parsed_data = []

        for row in csv_reader:
            if line_count >= line_offset:
                parsed_data.append(row)
            
            line_count += 1

        # Remove blank row
        if dataset_year == "2017":
            del parsed_data[-1]

        # Remove weird whitespaces
        if dataset_year == "2018":
            for i in range(1,len(parsed_data)):
                days = re.findall('[A-ZĄĆĘŁŃÓŚŻŹa-ząćęłńóśżź]', parsed_data[i][0])
                parsed_data[i][0] = ''.join(days)

        # Remove Summary row
        del parsed_data[-1]
    
    return parsed_data


def parse_csv_hours(path: str, line_offset: int, dataset_year: int):
    """

    """

    with open(path, encoding='cp1250') as file:
        csv_reader = csv.reader(file, delimiter=';')

        line_count = 0
        parsed_data = []

        for row in csv_reader:
            if line_count >= line_offset:
                parsed_data.append(row)

            line_count += 1

        # Remove blank row
        if dataset_year == "2017":
            del parsed_data[-1]

        # Remove weird whitespaces
        if dataset_year == "2018":
            for i in range(1,len(parsed_data)):
                days = re.findall('[A-ZĄĆĘŁŃÓŚŻŹa-ząćęłńóśżź]', parsed_data[i][0])
                parsed_data[i][0] = ''.join(days)

        # Remove Summary row
        del parsed_data[-1]

    return parsed_data
