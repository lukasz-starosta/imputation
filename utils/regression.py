import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


def regression(X, data, attribute_name, title):
    if len(data) == 0:
        print('Brak danych do wyświetlenia regresji.')
        return

    Y = data[attribute_name].values.reshape(-1, 1)
    X = X.values.reshape(-1, 1)

    linear_regression = LinearRegression()  # create object for the class
    linear_regression.fit(X, Y)  # perform linear regression
    Y_pred = linear_regression.predict(X)  # make predictions
    print('Parametry regresji liniowej: ', linear_regression.coef_, linear_regression.intercept_[0])

    plt.title(
        f'{title}\nAtrybut: {attribute_name}\nWsp. regresji: {linear_regression.coef_[0][0]}\n Wyraz wolny: {linear_regression.intercept_[0]}')
    plt.scatter(X, Y)
    plt.xlabel('Release date')
    plt.ylabel(attribute_name)
    plt.plot(X, Y_pred, color='red')
    plt.show()
