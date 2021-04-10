import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer



# def mice(filename):
    # mice_impute = IterativeImputer()
    # traindatafill = Mice_impute.fit_transform(traindata)
    # print(traindatafill)
df = pd.DataFrame({
    'age':[25,27,29,31,33,np.nan],
    'experience':[np.nan,3,5,7,9,11],
    'salary':[50,np.nan,80,90,100,130],
    'personal loan' : [1,1,0,0,1,0]
    })

X = df.drop('personal loan',1)
Y = df['personal loan']

print(X)
print(X.corr())

lr = LinearRegression()
imp = IterativeImputer(estimator=lr, verbose=2, max_iter=30, tol=1e-10,imputation_order='roman')

A = imp.fit(X)
B = imp.transform(X)
df.DataFrame.replace(B)

print(B)
