from collections import Counter
from math import sqrt
from utils.extract import extract
import pandas as pd

missing_indexes = []
non_missing_rows = []
non_missing_row_indexes = []
k = 20

# todo: low stats - possible error - to check
def hot_deck(filename):
    headers, names, numeric_data = extract(filename)
    row_length = len(numeric_data)
    column_length = len(numeric_data[0])

    # Scan for missing elements.
    for i in range(row_length):
        for j in range(column_length):
            # If not missing
            if numeric_data[i][j] != '':
                numeric_data[i][j] = float(numeric_data[i][j])

                # store indexes of rows with non-missing attributes
                non_missing_row_indexes.append(i)
                # Add elements to the NM array
                non_missing_rows.append(numeric_data[i])

            # If found a missing attribute:
            else:
                missing_indexes.append([i, j])

    # for each missing index, find the best fit
    for _, indexes in enumerate(missing_indexes):
        i, j = indexes
        euclidean = []
        euclideanTotal = 0

        # for each non missing row and column
        for r in range(len(non_missing_rows)):
            for c in range(column_length):
                # except itself
                if c != j and numeric_data[i][c] != '' and non_missing_rows[r][c] != '':
                    # calculate sum of euclidean distances
                    # between the missing and non-missing elements
                    euclideanTotal += (float(numeric_data[i][c]) -
                                       float(non_missing_rows[r][c])) ** 2

            # once the distances for all of the columns for a row have been summed
            # get the distance by sqrt of the sum
            euclidean_distance = sqrt(euclideanTotal)

            # Store found euclidean distance and index of current non-missing row
            euclidean.append([euclidean_distance, non_missing_row_indexes[r]])

        # Sort the euclidean list by the distance from low to high
        euclidean = sorted(euclidean, key=lambda l: l[0])

        # Gets k lowest distances
        first_k_values = [numeric_data[euclidean[r][1]][j] for r in range(k)]

        # Count the elements in the values
        elements = Counter(first_k_values)
        # Imputes the most common element from above list
        numeric_data[i][j] = elements.most_common(1)[0][0]

    # Writing data to new file
    data = []
    for i in range(len(names)):
        data.append([names[i]] + numeric_data[i])

    df = pd.DataFrame(data, columns=headers)
    return df
