import tensorflow as tf

# tf.placeholder(dtype, shape=None, name=None)
# TF provides a placeholder op that must be fed with data on execution
# Its value must be fed using the 'feed_dict' optional argument to
# Session.run(), Tensor.val(), or Operation.run()

# None means that its size is not yet determined
# We should specify dtype to let placeholder know which data will be fed into
x = tf.placeholder(tf.float32, [None, 3])
print(x)

# data that will be fed to placeholder x
# [None, 3] -> [2, 3]
x_data = [[1, 2, 3], [4, 5, 6]]

# class tf.Variable()
# Variable() constructor needs type and shape of tensor(Tensor) for initializing variable
# When learning a model, we use Variables to update and maintain parameters

# calling tf.Variable() adds operations to graph
# tf.random_normal() returns a tensor of the specified shape
# filled with random normal values(normal distribution)
weights = tf.Variable(tf.random_normal([3,2]), name="weights")
bias = tf.Variable(tf.random_normal([2,1]), name="bias")

expr = tf.matmul(x, weights) + bias

with tf.Session() as sess:
    # initialize Variables
    sess.run(tf.global_variables_initializer())
    print("=== x_data ===")
    print(x_data)
    print("=== W ===")
    print(sess.run(weights))
    print("=== b ===")
    print(sess.run(bias))
    print("=== expr ===")
    print(sess.run(expr, feed_dict={x: x_data}))