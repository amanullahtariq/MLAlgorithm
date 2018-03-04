# Load all usefull libraries
import pandas as pd
from  sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
import argparse

parser = argparse.ArgumentParser(description='Applying different machine learning model using scikit-learn')
parser.add_argument('--data_dir',
                    default='./input/sample.csv',
                    type=str,
                    help='A path to the csv file.')

parser.add_argument('--type',
                    default='knn',
                    type=str,
                    help='knn,all')


# Apply different machine learning algorithm and check there accruacy
def apply_machine_learning(X_train, X_test, y_train, y_test):
    dt_clf = tree.DecisionTreeClassifier()
    knnClf = KNeighborsClassifier(n_neighbors=20)
    rpcClf = RandomForestClassifier(n_estimators=30)
    adaBoostClf = AdaBoostClassifier()

    # Train
    clf = dt_clf.fit(X_train, y_train)
    # Predict

    prediction = clf.predict(X_test)

    # Explained variance score: 1 is perfect prediction
    print('Decision Tree Classifier')
    print('Score:  %.2f ' % accuracy_score(y_test, prediction))
    print('Variance score: %.2f' % clf.score(X_test, y_test))

    knnClf = knnClf.fit(X_train, y_train)
    prediction = knnClf.predict(X_test)

    # Explained variance score: 1 is perfect prediction
    print('KNeighbors Classifier')
    print('Score:  %.2f ' % accuracy_score(y_test, prediction))
    print('Variance score: %.2f' % knnClf.score(X_test, y_test))

    rpcClf = rpcClf.fit(X_train, y_train)
    prediction = rpcClf.predict(X_test)

    # Explained variance score: 1 is perfect prediction
    print('Random Forest Classifier')
    print('Score:  %.2f ' % accuracy_score(y_test, prediction))
    print('Variance score: %.2f' % rpcClf.score(X_test, y_test))

    adaBoostClf = adaBoostClf.fit(X_train, y_train)
    prediction = adaBoostClf.predict(X_test)

    # Explained variance score: 1 is perfect prediction
    print('Adaboost Classifier')
    print('Score:  %.2f ' % accuracy_score(y_test, prediction))
    print('Variance score: %.2f' % adaBoostClf.score(X_test, y_test))

    return prediction

# Visualizing KNN classifier and how we choose 'k'
def apply_knn(X_train, X_test, y_train, y_test):
    myList = list(range(1, 50))
    # subsetting just the odd ones
    neighbors = filter(lambda x: x % 2 != 0, myList)
    # empty list that will hold cv scores
    cv_scores = []

    # perform 10-fold cross validation
    for k in neighbors:
        knn = KNeighborsClassifier(n_neighbors=k)
        scores = cross_val_score(knn, X_train, y_train, cv=10, scoring='accuracy')
        cv_scores.append(scores.mean())
        print("K = ", k)
        print(scores)

    # changing to misclassification error
    MSE = [1 - x for x in cv_scores]

    # determining best k
    optimal_k = neighbors[MSE.index(min(MSE))]
    print "The optimal number of neighbors is %d" % optimal_k

    # plot misclassification error vs k
    plt.plot(neighbors, MSE)
    plt.xlabel('Number of Neighbors K')
    plt.ylabel('Misclassification Error')
    plt.show()


if __name__ == "__main__":
    args = parser.parse_args()
    data_path = args.data_dir
    type = args.type

    # 1) Load Data from the file
    df = pd.read_csv(data_path)
    # 295 features + label
    print ("Dimension of data {}".format(df.shape))

    # Removing un-important features
    index = []
    for i in range(0, len(df.columns)- 2):
        if df[df.columns[i]].mean() > 0 and df[df.columns[i]].quantile(0.75) > 0 and  df[df.columns[i]].quantile(0.75) != 1             and df[df.columns[i]].quantile(0.5) != 1 and df[df.columns[i]].quantile(0.25) != 1 :
            index.append(i)



    features = df[df.columns[index]]
    labels = df[df.columns[len(df.columns)-1]]

    print("Total Features: ", len(features.columns))

    X = features.values
    y = labels.values

    # #Split data-set into train and test
    X_train, X_test, y_train, y_test = train_test_split(features.values, labels.values, test_size=0.2, random_state=0)


    #3) Train
    if type == 'all':
        prediction = apply_machine_learning(X_train, X_test, y_train, y_test )
    else:
        apply_knn(X_train, X_test, y_train, y_test)