import pandas as pd

def regression(filename):
    df = pd.read_csv(filename)
    filled = pd.DataFrame()