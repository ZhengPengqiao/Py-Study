#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy

print('使用列表生成一维数组')
data = [1, 2, 3, 4, 5, 6]
x = numpy.array(data)
# 打印数组
print(x)
# 打印数组元素的类型
print(x.dtype)

print('使用列表生成二维数组')
data = [[1, 2], [3, 4], [5, 6]]
x = numpy.array(data)
# 打印数组
print(x)
# 打印数组的维度
print(x.ndim)
# 打印数组各个维度的长度。shape是一个元组
print(x.shape)

print('使用zero/ones/empty创建数组:根据shape来创建')
# 创建一维长度为6的，元素都是0一维数组
x = numpy.zeros(6)
print(x)
# 创建一维长度为2，二维长度为3的二维0数组
x = numpy.zeros((2, 3))
print(x)
# 创建一维长度为2，二维长度为3的二维1数组
x = numpy.ones((2, 3))
print(x)
# 创建一维长度为2，二维长度为3,未初始化的二维数组
x = numpy.empty((3, 3))
print(x)

print('使用arrange生成连续元素')
# [0,1,2,3,4,5,] 开区间
print(numpy.arange(6))
# [0, 2，4]
print(numpy.arange(0, 6, 2))
