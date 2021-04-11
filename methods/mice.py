#from fancyimpute import KNN, NuclearNormMinimization, SoftImpute, BiScaler, IterativeImputer
import numpy as np
import pandas as pd
from tabulate import tabulate


def mice(filename):
    '''df = pd.read_csv(filename)
    df = df.drop('Model',1)
    MICE_imputer = IterativeImputer()
    df_MICE = df.copy(deep= True)
    df_MICE.iloc[:, :] = MICE_imputer.fit_transform(df_MICE)
    return df_MICE'''
