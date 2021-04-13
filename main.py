import argparse
import sys

import pandas as pd

from methods.hot_deck import hot_deck
from methods.interpolate import interpolate
from methods.mean import mean_imputation
from methods.mice import mice
from utils.basic_statistics import basic_statistics
from utils.hypothesis import check_mean_value_hypothesis
from utils.regression import regression
from methods.regression_fill import regression_fill

attribute_mean_val_hypotheses = {"Price": 460, "Max resolution": 2475, "Zoom tele (T)": 120}

dataset_paths = ["dataset/camera_dataset.csv",
                 "dataset/output_missing_5.csv",
                 "dataset/output_missing_15.csv",
                 "dataset/output_missing_30.csv",
                 "dataset/output_missing_45.csv"]

parser = argparse.ArgumentParser(description='Imputation methods')
choices = {'hotdeck': hot_deck, 'interpolate': interpolate, 'mean': mean_imputation, 'mice': mice,
           'regression': regression_fill}

parser.add_argument('-m', '--method',
                    type=str,
                    help='The imputation method to use', choices=choices.keys(), required=True)

# parser.add_argument('-f', '--filename',
#                     type=str,
#                     help='The filename on which the operation will be performed', required=True)

args = parser.parse_args()
method = args.method

if method in choices:
    for path in dataset_paths:
        print(f"ZBIÓR: {path}")
        print(f"PRZED IMPUTACJĄ")
        df = pd.read_csv(path)

        attributes_for_regression=["Max resolution", "Price"]
        # dfnona = df.dropna()
        basic_statistics(df)
        for attribute_name, mean_value_hypothesis in attribute_mean_val_hypotheses.items():
            check_mean_value_hypothesis(df, attribute_name, mean_value_hypothesis)
            # basic_statistics(dfnona)
            # regression(dfnona['Release date'], dfnona, attribute_name, title=f"Metoda: {method} - Przed imputacją, zbiór '{path}'")
        for at in attributes_for_regression:
            dfnona = df[["Release date", at]].dropna()
            regression(dfnona['Release date'], dfnona, at,
                   title=f"Metoda: {method} - Przed imputacją, zbiór '{path}'")
        print(f"PO IMPUTACJI METODĄ {method}")
        # choices[method](args.filename)
        df = choices[method](path)

        basic_statistics(df)
        for attribute_name, mean_value_hypothesis, in attribute_mean_val_hypotheses.items():
            check_mean_value_hypothesis(df, attribute_name, mean_value_hypothesis)
            # regression(df['Release date'], df, attribute_name, title=f"Metoda: {method} - Po imputacji, zbiór '{path}'")
        for at in attributes_for_regression:
            regression(df['Release date'], df, at, title=f"Metoda: {method} - Po imputacji, zbiór '{path}'")
        print("\n")
else:
    print('Method not found.')
    sys.exit()
