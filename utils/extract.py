import csv


def extract(filename):
    # Table headers
    headers = []
    # First column of the table
    names = []
    # All other columns of the table
    numeric_data = []

    with open(filename) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')

        for row in reader:
            if reader.line_num == 1:
                headers = row
            elif len(row) > 0:
                names.append(row[0])
                # Extract the numeric data (all but first column)
                numeric_data.append(row[1:])

    return headers, names, numeric_data
