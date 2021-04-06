import pandas as pd

def interpolation_imputation(df):
    filled = pd.DataFrame()
    for (columnName, columnData) in df.iteritems():
        filled[columnName] = columnData.fillna(columnData.interpolate().fillna(method='bfill'))
    return filled