import pandas as pd

def parse_xlsx_place_characteristics(path: str, line_offset: int):
    """
    Function used to parse xlsx dataset place characteristics
    """
    
    df = pd.read_excel(path, sheet_name='Charkat. miejsca zdarzenia')

    parsed_data = df[line_offset:-1].values.tolist()

    return parsed_data

def parse_xls_place_characteristics(path: str, line_offset: int):
    """
    Function used to parse xls dataset place characteristics
    """

    df = pd.read_excel(path)#, sheet_name='Charkat. miejsca zdarzenia')

    parsed_data = df[line_offset:-1].values.tolist()

    return parsed_data

def parse_2015_xls_dataset(path: str, sheet_name: str, line_offset: int):
    """
    Function used to parse whole xls aggregated dataset
    """

    df = pd.read_excel(path, sheet_name = sheet_name)

    parsed_data = df[line_offset:].values.tolist()

    result = []

    for row in parsed_data:
        result.append([ row[0],
                        row[2],
                        row[4],
                        row[6],
                        row[8]])

    for line in result:
        line.append('2015')

    #print(result)

    return result
