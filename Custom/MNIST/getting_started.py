import numpy as np
import tensorflow as tf

def test_run():

    # Declare list of features. We only have one real-valued feature. There are many
    # other types of columns that are more complicated and useful.
    features = [tf.contrib.layers.real_valued_column("x", dimension=1)]

    # An estimator is the front end to invoke training (fitting) and evaluation
    # (inference). There are many predefined types like linear regression,
    # logistic regression, linear classification, logistic classification, and
    # many neural network classifiers and regressors. The following code
    # provides an estimator that does linear regression.
    estimator = tf.contrib.learn.LinearRegressor(feature_columns=features)

    # TensorFlow provides many helper methods to read and set up data sets.
    # Here we use `numpy_input_fn`. We have to tell the function how many batches
    # of data (num_epochs) we want and how big each batch should be.
    x = np.array([1., 2., 3., 4.])
    y = np.array([0., -1., -2., -3.])
    input_fn = tf.contrib.learn.io.numpy_input_fn({"x":x}, y, batch_size=4,num_epochs=1000)

    # We can invoke 1000 training steps by invoking the `fit` method and passing the
    # training data set.
    estimator.fit(input_fn=input_fn, steps=1000)

    # Here we evaluate how well our model did. In a real example, we would want
    # to use a separate validation and testing data set to avoid overfitting.
    print(estimator.evaluate(input_fn=input_fn))

def run():
    #Model Parameters 
    W = tf.Variable([0.3], tf.float32)
    b = tf.Variable([0.3], tf.float32)

    #Model input and outputs 
    x = tf.placeholder(tf.float32)
    y = tf.placeholder(tf.float32)
    
    #Model
    linear_model = W * x + b

    #Loss
    loss = tf.reduce_sum(tf.square(linear_model - y))

    #optimizer
    optimizer = tf.train.GradientDescentOptimizer(0.01)
    train = optimizer.minimize(loss)

    #train data
    x_train = [1,3,2,4]
    y_train = [0,-2,-1,-3]

    #initialization
    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)

    # training loop
    for i in range(1000):
        sess.run(train, {x: x_train, y: y_train})
    
    #evaluate training accuracy
    curr_W, curr_b, curr_loss =  sess.run([W,b, loss], {x: x_train, y: y_train})
    print("W: %s b: %s Loss: %s" %(curr_W, curr_b, curr_loss))

if __name__ == '__main__':
    #run()
    test_run()