
import matplotlib.pyplot as plt
import csv
import numpy as np

X = []
y = []

reader = csv.reader(open("hums_out.csvunix.csv"))
for row in reader:
    X.append(row[0])
    y.append(row[1])

lw = 2
plt.scatter(X, y, color='darkorange', label='data')
#plt.plot(X_test, y_rbf, color='navy', lw=lw, label='RBF model')
# plt.plot(X, y_lin, color='c', lw=lw, label='Linear model')
# plt.plot(X, y_poly, color='cornflowerblue', lw=lw, label='Polynomial model')
plt.xlabel('time')
plt.ylabel('temperature')
plt.title('Support Vector Regression')
plt.legend()
plt.show()