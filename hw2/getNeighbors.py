# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:46:02 2019

Ref:https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/
@author: 105502506
"""

import euclideanDistance as eD
import operator
def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = eD.euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist, trainingSet[x]))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors


def main():
    trainSet = [[2, 2, 2, 'a'], [4, 4, 4, 'b']]
    testInstance = [5, 5, 5]
    k = 1
    neighbors = getNeighbors(trainSet, testInstance, k)
    print(neighbors[0])
    
if __name__ == "__main__":
    main()