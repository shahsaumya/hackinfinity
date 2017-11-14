print(__doc__)

import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import csv

from sklearn.model_selection import TimeSeriesSplit

from sklearn import preprocessing

# #############################################################################
# Generate sample data

X = []
y = []

reader = csv.reader(open("temp_sample.csv"))
for row in reader:
	X.append(row[0])
	y.append(row[1])

y = preprocessing.scale(y)
X = np.asarray(X)
X = X.astype(np.int)
print (X.shape)
X_train = np.empty([X.shape[0],])
y = np.asarray(y)
y = y.astype(np.int)
print (y.shape)
y_train = np.empty([y.shape[0],])

for i in range(X.shape[0]):
	#print (i)
	X_train[i] = np.asscalar(X[i])
	y_train[i] = np.asscalar(y[i])


X_train = X_train.reshape(-1,1)

tscv = TimeSeriesSplit(n_splits=3)
print(tscv)  

for train_index, test_index in tscv.split(X):
   print("TRAIN:", train_index, "TEST:", test_index)
   X_train, X_test = X[train_index], X[test_index]
   y_train, y_test = y[train_index], y[test_index]

X_test = X_test.reshape(-1,1)
X_train = X_train.reshape(-1,1)

# #############################################################################
# Fit regression model
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_lin = SVR(kernel='linear', C=1e3)
# svr_poly = SVR(kernel='poly', C=1e3, degree=2)
y_rbf = svr_rbf.fit(X_train, y_train).predict(X_test)
y_lin = svr_lin.fit(X_train, y_train).predict(X_test)
# y_poly = svr_poly.fit(X_train, y_train).predict(X_test)

# #############################################################################
# Look at the results
lw = 2
plt.scatter(X, y, color='darkorange', label='data')
plt.plot(X_test, y_rbf, color='navy', lw=lw, label='RBF model')
plt.plot(X, y_lin, color='c', lw=lw, label='Linear model')
# plt.plot(X, y_poly, color='cornflowerblue', lw=lw, label='Polynomial model')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend()
plt.show()