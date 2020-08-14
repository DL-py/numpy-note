"""
numpy：数组运算工具箱
1.使用时需要加入import numpy as np
"""
import numpy as np
# 方法与函数的区别：
a = np.arange(10)
sum1 = np.sum(a)  # 函数：对传输的参数作用
sum2 = a.sum()  # 方法：与对象相关联
"""
注意事项：
"""
a = np.random.randn(5)  # 尽量不要使用这种形式
# a.shape:(5,)
# a: [ 0.8083534  -0.150945    1.2177874  -2.02563605  0.99752628]
# a.T: [ 0.8083534  -0.150945    1.2177874  -2.02563605  0.99752628]
# a*a.T： 是一个数而不是一个矩阵
a = np.random.randn(5, 1)
# a:              a.shape:(5, 1)  a.T: [[-0.50059014  0.75734509  0.65669258  0.1199059  -0.91792297]]
# [[-0.94972553]
#  [ 0.22598457]
#  [-2.14889243]
#  [-1.44606478]
#  [ 0.0759098 ]]
# a.T.shape:(1, 5)
# a*a.T:
# [[ 0.23818033 -0.94090208 -0.29373558  0.68128673  0.1269009 ]
#  [-0.94090208  3.71691791  1.16036626 -2.69133941 -0.50130639]
#  [-0.29373558  1.16036626  0.36224902 -0.84019597 -0.15650037]
#  [ 0.68128673 -2.69133941 -0.84019597  1.94874033  0.36298505]
#  [ 0.1269009  -0.50130639 -0.15650037  0.36298505  0.06761196]]
# assert(a.shape == (5, 1))  # 通过这种方式，若a.shape！=（5， 1）就会报错
# dot是矩阵相乘，而*是数乘
a = np.random.randn(3, 3)
b = np.random.randn(3, 1)
c = a*b
c = np.dot(a, b)

