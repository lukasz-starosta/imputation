import pandas as pd
from sklearn.linear_model import LinearRegression
import os


def regression_fill(incomplete_filename):
    complete_filename = os.path.abspath("dataset/camera_dataset.csv") #because path as a string didn't work for some reason
    incomplete_data = pd.read_csv(incomplete_filename)
    complete_data = pd.read_csv(complete_filename)
    filled_data = pd.read_csv(incomplete_filename) #creating a copy of incomplete_data to fill its nans with predicted values
    complete_data = complete_data.dropna() #to be sure there is no nan value

    if(len(incomplete_data) == 0 or len(complete_data) == 0):
        print('Brak danych do obliczenia regresji liniowej.')
        return

    X_args = complete_data["Release date"]
    X_args = X_args.values.reshape(-1, 1)

    skipFirst = True
    for (columnName, columnData) in complete_data.iteritems():
        if skipFirst:
            skipFirst=False
            continue

        # counting the linear regression slope for complete data
        model = LinearRegression().fit(X_args, columnData)
        slope = model.coef_
        print(f"The slope coefficient of {columnName} attribute is: {slope}")

        predicted_data = model.predict(X_args) #array of all predicted values

        #putting the predicted values to the matrix if value is nan
        for i in range(len(predicted_data)):
            if pd.isna(incomplete_data.at[i, columnName]):
                filled_data.at[i, columnName] = predicted_data[i]
                #print(filled_data.at[i, columnName])

    return filled_data
