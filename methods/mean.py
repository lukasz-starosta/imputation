import pandas as pd

def mean_imputation(filename):
    df = pd.read_csv(filename)
    filled = pd.DataFrame()
    skipFirst = True
    for (columnName, columnData) in df.iteritems():
        if skipFirst:
            skipFirst=False
            continue
        filled[columnName] = columnData.fillna(columnData.mean())
    return filled