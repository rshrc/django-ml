import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

from .script_loader import Loader
# Importing the dataset
dataset = pd.read_csv('data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1 / 3, random_state=0)

# Fitting Simlple Regression Data Set into Training Set
print("X_test")
print(X_test)

regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print(y_pred)

filename = 'model.sav'

pickle.dump(regressor, open(filename, 'wb'))

print("Loading later")

loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.predict(X_test)
print(result)



# class Loader:
#
#     def __init__(self, filename, X_test):
#         self.filename = filename
#         self.X_test = X_test
#
#     def load(self):
#         loaded_model = pickle.load(open(self.filename, 'rb'))
#         result = loaded_model.predict(self.X_test)
#         return result


obj = Loader(filename, [[9]])

print("Using a class")
print(obj.load())
