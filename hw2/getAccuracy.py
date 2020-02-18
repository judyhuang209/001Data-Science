# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:43:09 2019

Ref: https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/
@author: 105502506
"""

def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0


def main():
    testSet = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
    predictions = ['a', 'a', 'a']
    accuracy = getAccuracy(testSet, predictions)
    print(accuracy)
    
if __name__ == "__main__":
    main()