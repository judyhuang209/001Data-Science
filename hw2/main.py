# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:51:15 2019

Ref:https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/
@author: 105502506
"""

import loadDataset as lD
import getNeighbors as gN
import getResponse as gR
import getAccuracy as gA

def main():
	# prepare data
    trainingSet=[]
    testSet=[]
    split = 0.5
    lD.loadDataset('iris.data', split, trainingSet, testSet)
    print ('Train set: ' + repr(len(trainingSet)))
    print ('Test set: ' + repr(len(testSet)))
    
	# generate predictions
    for k in range(1,21):
        predictions=[]
        for x in range(len(testSet)):
            neighbors = gN.getNeighbors(trainingSet, testSet[x], k)
            result = gR.getResponse(neighbors)
            predictions.append(result)
            #print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
        accuracy = gA.getAccuracy(testSet, predictions)
        print('Accuracy(k=' + repr(k) + '): ' + repr(accuracy) + '%')
        
main()