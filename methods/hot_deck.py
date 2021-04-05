from utils.extract import extract


def hot_deck(filename):
    names, headers, numeric_data = extract(filename)
    row_length = len(numeric_data)
    column_length = len(numeric_data[0])
