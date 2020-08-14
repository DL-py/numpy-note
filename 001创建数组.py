"""
创建数组：
1.创建数组时可以加入dtype来指定元素的数据类型
"""
import numpy as np
"""
1.1 利用array创建数组
1.作用：将原数据类型转化数组类型
2. 可以用于转换的数据类型：
数组，字典，range()等
3.dtype:用于指定数组元素的数据类型
"""

a = np.array([1, 2, 3, 4])
a = np.array([1, 2, 3, 4], dtype='float32')  # float32类型
a = np.array({'a': 1, 'b': 2, 'c': 3})

"""
1.2 利用arange函数
np.arange(start, stop, steps, dtype)
"""
b = np.arange(10, dtype=np.uint8)  # 默认从0开始
b = np.arange(1, 10, 2)  # [1 3 5 7 9]

"""
1.3 利用np.linspace函数
np.linspace(start, stop, nums)
"""
b = np.linspace(-10, 10, 100)  # 表示从-10到10生成100个数据，首尾都会包含在内

"""
1.3 创建一个特殊的数组
eg:np.ones(shape, dtype)

"""
'''
np.ones(shape, dtype) 
shape:int、列表、元组、range
shape如(2, 3),其中最后一个数字即3表示一维数组中的列,一次类推
类似函数：np.zeros
'''
c = np.ones((2, 3))  # 2*3的数组
c = np.ones(3)  # 1*3的数组
c = np.zeros([1, 2])
'''
np.random.randn()
1. 生成标准正态分布的数据
'''
np.random.seed(1)  # 用来保证每次生成的随机数是相同的
a = np.random.randn(3, 5)  # 这里只能用整数，不能用元组或列表
'''
np.random.randint(low, high=None, size=None, dtype)
*. 在[low, high)离散的等概率的生成整数
*. 若high=None, 则范围是[0, low)
size:整型或元组类型，表示返回结果的形状，默认生成一个标量
'''
a = np.random.randint(10, size=10)
b = np.random.randint (0, 16, (4, 4))







