import operator
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

def classify(input_x, features, labels, k):
    """
    TODO: in this function, you have to implement the KNN classifier as professor told during lecture, see more detail in the announcement.
    :param input_x: target of expected predict
    :param features: features of training data
    :param labels: labels of training data
    :param k: number of k-nearest
    :return: predicted label
    """
    distances = []
    for i in range(len(features)):
        distance = 0
        for j in range(len(input_x)):
            distance += pow((input_x[j] - features[i][j]), 2)
        distance = pow(distance, 0.5)
        # print("d: ", distance)
        # print("i: ", labels[i])
        distances.append((distance, labels[i]))
    distances= sorted(distances, key=operator.itemgetter(0))
    # print("D: ", distances)
    
    neighbors = []
    for i in range(k):
        neighbors.append(distances[i])
    # print("N: ", neighbors)
    
    classVotes = {}
    for i in range(k):
        result = neighbors[i][-1]
        
        # if the target IS the test data
        if neighbors[i][0] == 0:
            # print("bye!")
            return neighbors[i][-1]
        
        # W = 1/distance
        if result in classVotes:
            classVotes[result] += 1/neighbors[i][0]
        else:
            classVotes[result] = 1/neighbors[i][0]
                
    # print("v: ", classVotes)
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    # print("s: ", sortedVotes)
    # print("r: ", sortedVotes[0][0])
    return sortedVotes[0][0]
    
def predict(X, k):
    y = []
    for i in X:
        y.append(classify(i, X_train, y_train, k))
    return y


if __name__ == '__main__':
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.5, random_state=0,
                                                        stratify=iris.target)

    test_data_acc = []
    for i in range(1, 21):
        y_predict_test_data = predict(X_test, i)
        # print(y_test, "<->", y_predict_test_data)
        test_data_acc.append(accuracy_score(y_test, y_predict_test_data))

    k = range(1, 21)
    df = pd.DataFrame({
        'test_data_acc': test_data_acc
    }, index=k)
    print(df)

    test_data_acc.insert(0, None)
    plt.xlabel('Number of k')
    plt.ylabel('Accuracy')
    plt.xlim((1, 20))
    plt.plot(test_data_acc, label='test_data')
    plt.legend()
    plt.show()
