import tensorflow as tf

# generates constant tensor
# tf.constant(value, dtype=None, shape=None, name='Const')

# make constant tensor with string value
hello = tf.constant('Hello, TensorFlow!')
print(hello)

# Constant 1-D tensor populated with value list
# if shape is not specified, shape is determined according to value
# [1, 2, 3, 4, 5, 6, 7]
tensor = tf.constant([1, 2, 3, 4, 5, 6, 7])
print(tensor)

# Constant 2-D tensor populated with scalar value -1
# value is a just scalar
# [[-1. -1. -1.]
#  [-1. -1. -1.]]
tensor2 = tf.constant(-1.0, shape=[2,3])

a = tf.constant(10)
b = tf.constant(32)
c = tf.add(a, b) # a + b
print(c)

# sess = tf.Session()
# print(sess.run(hello))
# print(sess.run(tensor))
# print(sess.run(tensor2))
# print(sess.run([a, b, c]))
# sess.close()

with tf.Session() as sess:
    print(sess.run(hello))
    print(sess.run(tensor))
    print(sess.run(tensor2))
    print(sess.run([a, b, c]))