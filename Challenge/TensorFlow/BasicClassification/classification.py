import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv('input/data.csv')

#Remove columns we don't care about
dataframe = dataframe.drop(["index", "price", "sq_price"], axis=1 )

dataframe = dataframe[0:15]
dataframe.loc[:, ("y1")] = [1, 1, 1, 0, 0, 1, 0, 1, 1, 1,0,0,0,1,1]

dataframe.loc[:, ("y2")] = dataframe["y1"] == 0
dataframe.loc[:, ("y2")] = dataframe["y2"].astype(int)

inputX = dataframe.loc[: , ['area', 'bathrooms']].as_matrix()
inputY = dataframe.loc[:, ["y1", "y2"]].as_matrix()

#Parameters 
learning_rate = 0.00001
training_epochs = 2000
display_steps = 50
n_samples = inputY.size

# Okay TensorFlow, we'll feed you an array of examples. Each example will
# be an array of two float values (area, and number of bathrooms).
# "None" means we can feed you any number of examples

x = tf.placeholder(tf.float32, [None, 2])
W = tf.Variable(tf.zeros([2, 2]))
b = tf.Variable(tf.zeros([2]))

y_values = tf.add(tf.matmul(x,W),b)

## Now converting it into proabilities
y = tf.nn.softmax(y_values)

# feed in a matrix of labels
y_ = tf.placeholder(tf.float32, [None,2])

# Cost Function
cost = tf.reduce_sum(tf.pow(y_ - y, 2)) / (2*n_samples)

# Gradient Descent
optimizier = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

#Initialize variables and tensorflow session
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for i in range (training_epochs):
    sess.run(optimizier, feed_dict= {x: inputX, y_: inputY})

    # Display logs per epoch step   
    if (i)  % display_steps == 0:
        cc = sess.run(cost, feed_dict={x: inputX, y_: inputY})
        print("Training step:", '%04d' % (i), "Cost: :", "{:.9f}".format(cc) )

print("Optimization Done!")
training_cost = sess.run(cost, feed_dict={x: inputX, y_: inputY})
print ("Training cost=", training_cost, "W=", sess.run(W), "b=", sess.run(b), '\n')


print(sess.run(y, feed_dict={x: inputX}))