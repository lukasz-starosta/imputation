import csv
import sys
from random import randrange

filename = sys.argv[1]
percent_of_data_to_delete = int(sys.argv[2])
output_filename = sys.argv[3]

# Table headers
headers = []

# First column of the table
names = []
# All other columns of the table
numeric_data = []

# Reading data from file and deleting some of it
with open(filename) as csv_file:
    reader = csv.reader(csv_file, delimiter=',')

    for row in reader:
        if reader.line_num == 1:
            headers = row
        if reader.line_num != 1:
            names.append(row[0])
            # Extract the numeric data (all but first column)
            numeric_data.append(row[1:])

    column_length = len(numeric_data)
    row_length = len(numeric_data[0])

    number_of_items = column_length * row_length
    number_of_items_to_delete = number_of_items * (percent_of_data_to_delete / 100)

    number_of_deleted_items = 0
    while number_of_deleted_items < number_of_items_to_delete:
        random_column = randrange(0, column_length - 1)
        random_row = randrange(0, row_length - 1)

        if numeric_data[random_column][random_row] is not None:
            numeric_data[random_column][random_row] = None
            number_of_deleted_items += 1

    # Writing data to new file
    writer = csv.writer(open(output_filename, 'w'), delimiter=",")

    writer.writerow(headers)
    for i in range(len(names)):
        writer.writerow([names[i]] + numeric_data[i])

print(f'Deleted: {percent_of_data_to_delete}% data. Output saved to {output_filename}')
