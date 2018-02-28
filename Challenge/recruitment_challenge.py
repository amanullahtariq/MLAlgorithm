# Load all usefull libraries
import pandas as pd
from  sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.gaussian_process.kernels import RBF
from sklearn import svm


# Load Data from the file
df = pd.read_csv('/media/aman/Work/thesis_data/hams_data/sample.csv')
# 295 features + label
print ("Dimension of data {}".format(df.shape))

# Validate dataset
features = df[df.columns[0:294]]
labels = df[df.columns[295]]


labels.replace('A', 1).replace('B' , 2).replace('C', 3).replace('D', 4).replace('E', 5)

# Split data-set into train and test
X_train, X_test, y_train, y_test = train_test_split(features.values, labels.values, test_size=0.4, random_state=0)

#print()



print ("Dimension of features {}".format(X_train.shape))
print ("Dimension of labels {}".format(X_test.shape))


# Apply machine learning
clf = tree.DecisionTreeClassifier()

#Train
clf = clf.fit(X_train, y_train)


# Predict

prediction = clf.predict(X_test)


# Explained variance score: 1 is perfect prediction
print('Decision Tree Classifier')
print('Score:  %.2f ' % accuracy_score(y_test, prediction))
print('Variance score: %.2f' % clf.score(X_test, y_test))


svmClf = svm.SVC(kernel='linear', C=5).fit(X_train, y_train)
prediction = svmClf.predict(X_test)

print('SVM Classifier')
print('Score:  %.2f ' % accuracy_score(y_test, prediction))
print('Variance score: %.2f' % svm.score(X_test, y_test))


#
#
# knnClf = KNeighborsClassifier()
#kernel = 1.0 * RBF([1.0])
#gpcClf = GaussianProcessClassifier(kernel=kernel)
# # allowing bootstrap
# rpcClf = RandomForestClassifier(bootstrap=True)
# adaBoostClf = AdaBoostClassifier()
#
# knnClf = knnClf.fit(X_train, y_train)
# prediction = knnClf.predict(X_test)
#
# # Explained variance score: 1 is perfect prediction
# print('KNeighbors Classifier')
# print('Score:  %.2f ' % accuracy_score(y_test, prediction))
# print('Variance score: %.2f' % knnClf.score(X_test, y_test))

#
# gpcClf = gpcClf.fit(X_train, y_train)
# prediction = gpcClf.predict(X_test)
#
# print('Guassian Process Classifier')
# # Explained variance score: 1 is perfect prediction
# print( 'Score:  %.2f ' % accuracy_score(y_test, prediction))
# print('Variance score: %.2f' % gpcClf.score(X_test, y_test))

#
# rpcClf = rpcClf.fit(X_train, y_train)
# prediction = rpcClf.predict(X_test)
#
# # Explained variance score: 1 is perfect prediction
# print('Random Forest Classifier')
# print( 'Score:  %.2f ' % accuracy_score(y_test, prediction))
# print('Variance score: %.2f' % rpcClf.score(X_test, y_test))



