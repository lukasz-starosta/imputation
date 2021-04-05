import csv
import sys
from random import randrange
from extract import extract

filename = sys.argv[1]
percent_of_data_to_delete = int(sys.argv[2])
output_filename = sys.argv[3]

names, headers, numeric_data = extract(filename)

# Reading data from file and deleting some of it
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
