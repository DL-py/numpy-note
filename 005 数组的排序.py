import numpy as np
"""
数组的排序
np.sort(a, axis=-1)
*. axis默认是在单数第一个维度中进行排序的
"""
# 一维数组：
a = np.array([4, 3, 5, 2])
a.sort()
# 二维数组：
b = np.random.randint(1, 16, size=(4, 4))
b.sort()  # 按行进行排序
b.sort(axis=0)  # 按列进行排序

# 三维数组
c = np.random.randint(1, 16, (2, 3, 4))
c.sort()  # 对其中每个二维矩阵按行进行排序
c.sort(axis=1)  # 对其中每个二维矩阵按列进行排序

