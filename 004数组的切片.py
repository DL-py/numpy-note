import numpy as np
"""
切片：
"""
"""
1.基本切片：选择多个数据
基本格式：
起始序号:终止序号:步长（每一维最多有2个：）
注意：
*. 切片不会改变数组的维数
*. 当某一位切片中只有：表示选择该维的所有的数据
*. 基本的切片不会生成一个副本，改变子集，原数组也会被改变
"""
# 一维数组切片
a = np.array([1, 2, 3, 4, 5, 6])
a[1:2]

# 二维数组切片
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
b[1:3, 2:3]

# 含有步长的切片
a[1:-1:2]  # 隔一个进行切片

# 缺少数据的切片
b[:, 1:3]  # ：表示选择维度0的全部数据

"""
2.索引与切片的混合使用：
*. 用于索引的维度：有1个[]
*. 用于切片的维度：有1~2个:
"""
b = np.arange(1, 17).reshape(4, -1)
b[:3:2, [1, 2]]
b[:3:2, [1, 2]]