import pandas as pd

def parse_xlsx_place_characteristics(path: str, line_offset: int, dataset_year: str):
    """

    """
    
    df = pd.read_excel(path, sheet_name='Charkat. miejsca zdarzenia')

    parsed_data = df[line_offset:-1].values.tolist()

    return parsed_data

def parse_xls_place_characteristics(path: str, line_offset: int, dataset_year: str):
    """

    """

    df = pd.read_excel(path)#, sheet_name='Charkat. miejsca zdarzenia')

    parsed_data = df[line_offset:-1].values.tolist()

    return parsed_data