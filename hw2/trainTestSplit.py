# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:13:41 2019

@author: user
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
X, y = np.arange(10).reshape((5, 2)), range(5)
print(X)
print(list(y))

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=0)

print('X_train:\n', X_train)
print('y_train:\n', y_train)

print('X_test:\n', X_test)
print('y_test:\n', y_test)

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.5, random_state=0,
                                                        stratify=iris.target)

print('X_train:\n', X_train)
print('y_train:\n', y_train)
print(len(X_train))
print(len(y_train))

print('X_test:\n', X_test)
print('y_test:\n', y_test)