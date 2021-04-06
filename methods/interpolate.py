from utils.extract import extract
import pandas as pd

def interpolate(filename):
    names, headers, numeric_data = extract(filename)
    row_length = len(numeric_data)
    column_length = len(numeric_data[0])
    df = pd.read_csv(filename)
    print(df)
    return df
