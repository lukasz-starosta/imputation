import pandas as pd
import numpy as np
from tabulate import tabulate

condition = lambda column : (column != 'Model' and column != 'Release date')

def basic_statistics(df):
    new_df = []
    columns = []
    for column in df:
        if condition(column):
            #-----------srednia------------
            mean = df[column].mean()
            mean = round(mean,2)
            #----odchylenie standardowe----
            std = df[column].std()
            std = round(std,2)
            #-----------moda---------------
            mode = df[column].mode()
            try:
                mode = round(mode[0])
            except KeyError:
                print('This data frame lacks too much data!')

            #-----------mediana------------
            md = df[column].median()
            md = round(md,2)
            #-----------kwartyl------------
            qt = df[column].quantile()
            qt = round(qt,2)


            new_df.append([mean,std, mode, mode, qt])
            columns.append(column)



    new_df = pd.DataFrame(new_df, index=columns)
    print('\n',tabulate(new_df, headers = ['mean','std','mode','md','qt']),'\n')
    return new_df
        