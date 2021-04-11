import pandas as pd
from sklearn.linear_model import LinearRegression

def regression(filename):
    complete_data = pd.read_csv('../dataset/camera_dataset.csv')
    incomplete_data = pd.read_csv(filename)
    filled_data = pd.DataFrame()
    data_without_nans = incomplete_data.dropna()  # removes rows with missing data

    if(len(incomplete_data) == 0 or len(complete_data) == 0):
        print('Brak danych do obliczenia regresji liniowej.')
        return

    X_args = complete_data["Release date"]

    for (columnName, columnData) in complete_data:

        #counting the linear regression slope for complete data
        model = LinearRegression().fit(X_args, columnData)
        slope = model.coef__

        predicted_data = model.predict(X_args) #array of all predicted values

        #putting the predicted values to the matrix if value is nan
        for i in range(len(predicted_data)):
            if incomplete_data.iloc[i, columnName] is None:
                filled_data[i][columnName] = predicted_data[i]

        return filled_data
