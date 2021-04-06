import pandas as pd
from scipy import stats
from methods.interpolation import interpolation_imputation
from methods.mean import mean_imputation

MEAN_PRICE_HYPOTHESIS = 458

dataset_paths = ["dataset/camera_dataset.csv",
                 "dataset/output_missing_5.csv",
                 "dataset/output_missing_15.csv",
                 "dataset/output_missing_30.csv",
                 "dataset/output_missing_45.csv"]


for dataset_path in dataset_paths:
    print(f"zbiór: {dataset_path}")

    df = pd.read_csv(dataset_path)

    _, p_val = stats.ttest_1samp(df["Price"], MEAN_PRICE_HYPOTHESIS, nan_policy="omit")
    print(f"p-wartość dla hipotezy o średniej cenie wynoszącej {MEAN_PRICE_HYPOTHESIS} przed imputacją: {p_val}")
    #todo: jeszcze 2 hipotezy
    #todo: analiza średniej, odchylenia standardowegwo, mediany, mody, kwartyli
    #todo: analiza krzywej regresji


    # df = mean_imputation(df)
    df = interpolation_imputation(df)
    df.to_csv("test.csv")

    _, p_val = stats.ttest_1samp(df["Price"], MEAN_PRICE_HYPOTHESIS)
    print(f"p-wartość dla hipotezy o średniej cenie  po imputacji: {p_val}")
    # todo: jeszcze 2 hipotezy
    # todo: analiza średniej, odchylenia standardowegwo, mediany, mody, kwartyli
    # todo: analiza krzywej regresji


