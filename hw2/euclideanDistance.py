# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:00:49 2019

Ref: https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/
@author: 105502506
"""

import math
def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)

# test
def main():
    data1 = [1, 2, 3, 'a']
    data2 = [3, 2, 1, 'b']
    distance = euclideanDistance(data1, data2, 3)
    print ('Distance: ' + repr(distance))

if __name__ == "__main__":
    main()