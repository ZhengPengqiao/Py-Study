#!/usr/bin/python3

import sys
import time
import numpy as np

"""
    该段代码演示了python中的向量加法
    使用如下指令运行程序:
        python vectorsum.py n
    n为指定向量的大小的整数

    加法中的第一个向量包含了0到n的整数的平方
    第二个向量包含了0到n的整数的立方
    程序将打印出向量加和后的最后两个元素和消耗的时间
"""

def numpysum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b
    return c

def pythonvectorsum(n):
    a = list(range(n))
    b = list(range(n))
    c = []

    for i in range(len(a)):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i] + b[i])

    return c

size = int(sys.argv[1])

start = time.time()
c = pythonvectorsum(size)
delta = time.time() - start
print("The last 2 elements of the sum",c[-2:])
print("pythonvectorsum elapsed time in microseconds" ,delta)

start = time.time()
c = numpysum(size)
delta = time.time() - start
print("The last 2 elements of the sum",c[-2:])
print("numpyvectorsum elapsed time in microseconds" ,delta)
