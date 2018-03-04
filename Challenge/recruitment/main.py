# Load all usefull libraries
import pandas as pd
import numpy as np
import argparse
from knn_classifier import KnnClassifier
import timeit


parser = argparse.ArgumentParser(description='Run knn classifier manually')
parser.add_argument('--data_dir',
                    default='./input/sample.csv',
                    type=str,
                    help='A path to the csv file.')



# Method to calculate the accuracy
# By dividing the correct predictions by total number of outputs
def accuracy_score(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x] == predictions[x]:
            correct += 1
    return (correct / float(len(testSet))) * 100.0

# Split dataset in to train and test dataset
def train_test_split(X, Y, test_size=0.1):
    train_size = int(len(X) - len(X) * test_size)
    X_train = X[0:train_size]
    X_test = X[train_size:]

    Y_train = Y[0:train_size]
    Y_test = Y[train_size:]

    return X_train, X_test, Y_train, Y_test


if __name__ == "__main__":
    args = parser.parse_args()
    data_path = args.data_dir

    # Read data from the csv
    df = pd.read_csv(data_path)
    index = []

    # Removing unimportant features
    for i in range(0, len(df.columns) - 2):
        if df[df.columns[i]].mean() > 0 and df[df.columns[i]].quantile(0.75) > 0 and df[df.columns[i]].quantile(
                0.75) != 1 and df[df.columns[i]].quantile(0.5) != 1 and df[df.columns[i]].quantile(0.25) != 1:
            index.append(i)

    features = df[df.columns[index]]
    labels = df[df.columns[len(df.columns) - 1]]

    # Replacing alphabets to numbers for ease of use
    labels = labels.replace('A', 1).replace('B', 2).replace('C', 3).replace('D', 4).replace('E', 5)

    X = features.values
    y = labels.values


    X_train, X_test, Y_train, Y_test = train_test_split(features.values, labels.values, test_size=0.2)

    # Running knn classifier on the dataset
    start = timeit.default_timer()
    knnClf = KnnClassifier(X_train, Y_train)
    predictions = knnClf.predict(X_test=X_test, k=41)
    stop = timeit.default_timer()

    print ("Run Time: ", stop - start)

    # transform the list into an array
    predictions = np.asarray(predictions)
    # evaluating accuracy
    accuracy = accuracy_score(Y_test[0:100], predictions)
    print('\nThe accuracy of our classifier is %d%%' % accuracy )



