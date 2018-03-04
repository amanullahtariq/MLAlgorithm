import numpy as np
from collections import Counter

# K-nearest neighbor classifier class
# Predict block is responsible for finding out the correct prediction
class KnnClassifier():
    def __init__(self,X_train, Y_train):
        self.X_train = X_train
        self.Y_train = Y_train


    # Prediction model takes the input and returns the prediction
    # on the basis of the model function.
    # Returns a list of predictions against the input X_test
    def predict(self, X_test, k ):

        # check if k larger than n
        if k > len(self.X_train):
            raise ValueError

        self.X_test = X_test
        self.k = k

        predictions = []
        for i in range(len(self.X_test)):
            predictions.append(self.get_predictions(X_test[i,:]))
        return  predictions

    # Returns a prediction for the one class
    def get_predictions(self, x):

        euclidean_dist = []
        targets =[]

        for i in range(len(self.X_train)):
            # finding euclidean distance between the data points
            # and save it in the list
            dist = self.euclideanDistance(x, self.X_train[i,:])
            euclidean_dist.append([dist,i])

        euclidean_dist = sorted(euclidean_dist)

        for i in range(self.k):
            index = euclidean_dist[i][1]
            targets.append(self.Y_train[index])

        # return most common target
        return Counter(targets).most_common(1)[0][0]

    # For finding euclidean distance between two points
    def euclideanDistance(self,instance1, instance2):
        distance = np.sum(np.square(instance1-instance2))
        return np.sqrt(distance)

