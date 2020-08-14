"""
广播：
numpy中对于shape不同的数据，通过广播成相同的shape，再参与运算
"""
import numpy as np
"""
1.1 对于标量的广播
一般来说标量可以进行广播
"""
a = np.random.randn(2, 4)
b = 1
c = a + b  # + - * / % 与加法类似
"""
1.2 对向量进行广播

"""
a = np.random.randn(2, 4)
# 注意区别b1、b2、b3:
b1 = np.random.randn(2)
# b1 = [-1.91856112 -1.91333733] b1.shape = (2,)
b2 = np.random.randn(2, 1)
# b2 = [[1.00556851]             b2.shape = (2, 1)
#       [0.2581524 ]]
b3 = np.random.randn(1, 2)
# b3 = [[0.95164209 0.86447508]] b3.shape = (1, 2)

b = np.random.randn(4)
c = a + b  # a.shape = (2, 4) b.shape=(4, )时可以进行广播，b.shape(2,)不可以进行广播

"""
矩阵的广播
广播的条件：有一个维度为1，其余维度对应相等
"""
np.random.seed(1)
a = np.random.randn(3, 4)
b1 = np.random.randn(1, 4)  # 可以进行广播
b2 = np.random.randn(3, 1)  # 可以进行广播
b3 = np.random.randn(3, 2)  # 无法进行广播
b4 = np.random.randn(2, 4)  # 无法进行广播

a = np.zeros((2, 3, 4))
b1 = np.random.randn(1, 3, 4)  # 可以进行广播
b2 = np.random.randn(2, 1, 4)  # 可以进行广播
b3 = np.random.randn(2, 3, 1)  # 可以进行广播









