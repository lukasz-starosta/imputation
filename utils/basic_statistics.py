import pandas as pd
import numpy as np
from tabulate import tabulate


condition = lambda column : (column != 'Model' and column != 'Release date')

def basic_statistics(df):
    new_df = []
    columns = []

    mean = np.nan
    std = np.nan
    mode = np.nan
    md = np.nan
    qt1 = np.nan
    qt3 = np.nan

    # df.replace('', np.nan, inplace=True)
    # df.dropna(inplace=True)
    for column in df:
        if condition(column):
            try:
                #-----------srednia------------
                mean = df[column].dropna().mean()
                mean = round(mean,2)

                #----odchylenie standardowe----
                std = df[column].dropna().std()
                std = round(std,2)

                #-----------moda---------------
                mode = df[column].dropna().mode()
                mode = round(mode[0])

                #-----------mediana------------
                md = df[column].dropna().median()
                md = round(md,2)

                #-----------kwartyl 1------------
                qt1 = np.percentile(df[column].dropna(), 25)
                qt1 = round(qt1,2)

                #-----------kwartyl 3------------
                qt3 = np.percentile(df[column].dropna(), 75)
                qt3 = round(qt3,2)

            except KeyError:
                print('This data frame lacks too many data!')

            new_df.append([mean,std, mode, md, qt1, qt3])
            columns.append(column)

    new_df = pd.DataFrame(new_df, index=columns)
    print('\n',tabulate(new_df, headers = ['mean','std','mode','median','1st quartile', '3rd quartile']),'\n')
    return new_df
