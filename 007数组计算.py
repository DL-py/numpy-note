"""
numpy的计算:
"""
import numpy as np
"""
*. 矩阵运算：
"""
a = np.random.randn(2, 3)
b = np.random.randn(2, 3)
'''
矩阵中元素的运算：
注意：
1. 一般来说，参与运算的两个数组应该具有相同的shape
2. 对于shape不相同的数组，若能进行广播成相同的shape，再进行运算
'''
c = a + b
c = a - b
c = a * b
c = a / b

"""
*. 常用的数学函数：
"""
a = np.arange(1, 10)
'''
*.指数函数：
'''
ans = np.exp(a)
'''
*.对数函数：
'''
ans = np.log(a)  # 以e为底
ans = np.log10(a)  # 以10为底
ans = np.log2(a)  # 以2为底
'''
*.三角函数
'''
ans = np.sin(a)  # sin函数
ans = np.cos(a)  # cos函数
ans = np.tan(a)  # tan函数
'''
*.求和运算
keepdims:用于保证求和后的数组形状

'''
# 二维数组运算
a = np.random.randint(1, 16, (4, 4))
b1 = np.sum(a, axis=1, keepdims=True)  # 按行进行求和，keepdims=True,结果是(4, 1)反之，则为(4, )
b2 = np.sum(a, axis=0, keepdims=True)  # 按列求和
b3 = np.sum(a)  # 对整个二维矩阵求和










