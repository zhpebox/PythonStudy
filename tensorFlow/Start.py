import tensorflow as tf

matrix1 = tf.constant([[3.,3.]])
matrix2 = tf.constant([[2.],[2.]])

product = tf.matmul(matrix1,matrix2)

# 显示调用session
# sess = tf.Session()
# result = sess.run(product)

with tf.Session() as sess:
    result = sess.run([product])
    print(result)
    result2 = sess.run(product)
    print(result2)
