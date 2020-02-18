# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:10:32 2019

Ref: https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/
@author: 105502506
"""

import operator
def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]


def main():
    neighbors = [[1,1,1,'a'], [2,2,2,'b'], [3,3,3,'c']]
    response = getResponse(neighbors)
    print (response)
    
if __name__ == "__main__":
    main()