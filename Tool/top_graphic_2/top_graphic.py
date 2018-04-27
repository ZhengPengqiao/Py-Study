#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import os
import sys


if len(sys.argv) < 2:
	print("Used: ", sys.argv[0], " file_name")
	sys.exit()

file_name = sys.argv[1]

print("file_name:", sys.argv[1])

color = []
name = []
color.append('#FF0000')
color.append('#00FF00')
color.append('#0000FF')
color.append('#FFFF00')
color.append('#FF00FF')
name.append("user_system")
name.append("/system/bin/tvdecoderserver")
name.append("/system/bin/mediaserver")
name.append("com.txznet.txz:svr1")
name.append("com.txznet.txz")


arr_count=[] * len(name)
arrY= [[] for i in np.arange(len(name))]

# 记录cpu,和进程名的位置
cpu_index = -1
name_index = -1

# 读取文件中的数据
with open(file_name, 'r') as f:
	linea = f.readlines()

	for x in np.arange(len(linea)):
		# 解析用户占用和系统占用的资源
		if (("User" in linea[x]) and ("System"  in linea[x])):
			item = linea[x].split()
			use_val = sys_val = 0
			for i in np.arange(len(item)):
				if ("User" in item[i]):
					use_val = float(item[i+1].replace("%,",""))
				elif ("System" in item[i]):
					sys_val = float(item[i+1].replace("%,",""))
					arrY[0].append(use_val+sys_val)
		# 查看显示信息时,cpu和进程名的位置
		elif (("CPU%" in linea[x]) and ("Name"  in linea[x])):
			item = linea[x].split()
			for i in np.arange(len(item)):
				if ("CPU%" in item[i]):
					cpu_index = i
				elif ("Name" in item[i]):
					name_index = i
		# 按照各个程序名,记录cpu的占用
		elif ("User " not in linea[x]):
			item = linea[x].split()
			if ( (len(item) >= name_index) and (name_index != -1) and (cpu_index != -1) and (len(item) >= cpu_index) ):
				for x in np.arange(len(name)):
					if (name[x] == item[-1]):
						arrY[x].append(float(item[cpu_index].replace("%","")))


for x in np.arange(len(arrY)):
	print(name[x], "arrY[",x,"]=",len(arrY[x]), arrY[x])


# 打印表的名字和横纵轴的文字
plt.title("this cpu used", fontsize=24, color='#FF0000')
plt.xlabel("Time", fontsize=16)
plt.ylabel("CPU Used", fontsize=16)
plt.grid(True, color='g',linestyle='--',linewidth='1')
plt.ylim(0, 100)

# 标记一条刻度线
# plt.axhline(y=18, xmin=0, xmax=100, c='#FFFF00')
plt.yticks(np.arange(0, 101, 2))

# 绘制图形
for x in np.arange(len(name)):
	plt.plot(np.arange(0., len(arrY[x]), 1), arrY[x], c=color[x], label=name[x],)
plt.legend(loc='center left')
plt.show()