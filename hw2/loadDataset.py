# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 13:58:29 2019

Ref: https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/
@author: 105502506
"""

import csv
import random
def loadDataset(filename, split, trainingSet=[] , testSet=[]):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):
	        for y in range(4):
	            dataset[x][y] = float(dataset[x][y])
	        if random.random() < split:
	            trainingSet.append(dataset[x])
	        else:
	            testSet.append(dataset[x])

# test
def main():
    trainingSet=[]
    testSet=[]
    # load the data into Train and Test 
    loadDataset('iris.data', 0.5, trainingSet, testSet)
    print ('Train: ' + repr(len(trainingSet)) )
    print ('Test: ' + repr(len(testSet)) )

if __name__ == "__main__":
    main()