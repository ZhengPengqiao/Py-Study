#!/usr/bin/python3
#
import numpy as np
import matplotlib.pyplot as plt
import os


cnames = [
	'#FF0000',
	'#000000',
	'#0000FF',
	'#FFFF00',]


name = []
name.append("task1")
name.append("task2")
name.append("task3")
name.append("task4")

arrY = [[] for item in np.arange(len(name)) ]

# 生成数据
for x in np.arange(len(name)):
	arrY[x] = np.arange(60)*x


for x in np.arange(len(arrY)):
	print(name[x], "arrY[",x,"]=",len(arrY[x]))

# 打印表的名字和横纵轴的文字
plt.title("this cpu used", fontsize=24, color='#FF0000')
plt.xlabel("Time", fontsize=16)
plt.ylabel("CPU Used", fontsize=16)
plt.grid(True, color='g',linestyle='--',linewidth='1')
# plt.ylim(0, 50)

# 绘制图形
for x in np.arange(len(name)):
	plt.plot(np.arange(0., len(arrY[x]), 1), arrY[x], c=cnames[x], label=name[x],)
plt.legend(loc='upper left')
plt.show()
