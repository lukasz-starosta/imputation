import pandas as pd

def m_interpolate(filename):
    df = pd.read_csv(filename)
    df = df.fillna(df.mean())    
    print(df.to_string())
    
