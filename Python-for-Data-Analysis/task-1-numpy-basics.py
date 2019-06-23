#%% [markdown]
# #这100道练习，带你玩转Numpy
# Numpy是Python做数据分析所必须要掌握的基础库之一。本文内容由科赛网翻译整理自!(Github开源项目)[https://github.com/rougier/numpy-100](部分题目保留了原文作参考).

#%%
# 1.导入numpy库并简写为 np
import numpy as np

#%%
# 2.打印numpy的版本和配置说明
print(np.__version__)
np.show_config()

#%%
# 3.创建一个长度为10的空向量(提示: np.zeros)
Z = np.zeros(10)
print(Z)

#%%
# 4.如何找到任何一个数组的内存大小(提示: size, itemsize)
Z = np.zeros((10,10))
print("%d bytes" % (Z.size * Z.itemsize))

#%%
# 5.如何从命令行得到numpy中add函数的说明文档(提示: np.info)
numpy.info(numpy.add)

#%%
# 6.创建一个长度为10并且除了第五个值为1的空向量(提示: array[4])
Z = np.zeros(10)
Z[4] = 1
print(Z)

#%%
# 7.创建一个值域范围从10到49的向量(提示: np.arange)
Z = np.arange(10,50)
print(Z)

#%%
# 8.反转一个向量(第一个元素变为最后一个) (提示: array[::-1])
Z = np.arange(50)
Z = Z[::-1]
print(Z)

#%%
# 9.创建一个 3x3 并且值从0到8的矩阵(提示: reshape)
Z = np.arange(9).reshape(3,3)
print(Z)

#%%
# 10.找到数组[1,2,0,0,4,0]中非0元素的位置索引(提示: np.nonzero)
nz = np.nonzero([1,2,0,0,4,0])
print(nz)