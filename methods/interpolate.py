import pandas as pd

def interpolate(filename):
    df = pd.read_csv(filename)
    df = df.interpolate(method='linear')
    print(df.to_string())

