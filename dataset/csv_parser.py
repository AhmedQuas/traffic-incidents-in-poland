import csv
import re

def parse_csv(path: str, line_offset: int, dataset_year: int):
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
        if dataset_year == 2017:
            del parsed_data[-1]

        # Remove Summary row
        del parsed_data[-1]

    return parsed_data