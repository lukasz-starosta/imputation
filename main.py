import pandas as pd
from scipy import stats
from methods.interpolation import interpolation_imputation
from methods.mean import mean_imputation
import argparse
import sys
from methods.hot_deck import hot_deck
from methods.interpolate import interpolate

MEAN_PRICE_HYPOTHESIS = 458

dataset_paths = ["dataset/camera_dataset.csv",
                 "dataset/output_missing_5.csv",
                 "dataset/output_missing_15.csv",
                 "dataset/output_missing_30.csv",
                 "dataset/output_missing_45.csv"]

parser = argparse.ArgumentParser(description='Imputation methods')
choices = {'hotdeck': hot_deck, 'interpolate': interpolate, 'mean': mean_imputation}

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
        print(f"zbiór: {path}")

        df = pd.read_csv(path)

        _, p_val = stats.ttest_1samp(df["Price"], MEAN_PRICE_HYPOTHESIS, nan_policy="omit")
        print(f"p-wartość dla hipotezy o średniej cenie wynoszącej {MEAN_PRICE_HYPOTHESIS} przed imputacją: {p_val}")
        # todo: jeszcze 2 hipotezy
        # todo: analiza średniej, odchylenia standardowegwo, mediany, mody, kwartyli
        # todo: analiza krzywej regresji

        # choices[method](args.filename)
        df = choices[method](path)

        _, p_val = stats.ttest_1samp(df["Price"], MEAN_PRICE_HYPOTHESIS)
        print(f"p-wartość dla hipotezy o średniej cenie  po imputacji: {p_val}")

else:
    print('Method not found.')
    sys.exit()
