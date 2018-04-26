#!/usr/bin/python3.5
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
name.append("mediaserver")
name.append("tvdecoderserver")
name.append("com.txznet.txz:svr1")
name.append("pci6865_task")


# 将打印处理为单独的文件信息
for x in np.arange(len(name)):
	cmdstr = 'grep -nIR ' + name[x] + ' com7--20180426162450--.log | awk \'{print $4}\' >  ' + name[x] + '.txt';
	os.system(cmdstr)

arrCount=[]
arrY= [[] for i in np.arange(len(name))]

# 读取文件中的数据
for x in np.arange(len(name)):
	namestr = name[x]+'.txt'
	fp=open(namestr)
	count = 0
	for linea in fp.readlines():
	    arrY[x].append(float(linea.replace("\n","").replace("%","")))
	    count = count+1
	fp.close()
	arrCount.append(count)


for x in np.arange(len(arrY)):
	print(name[x], "arrY[",x,"]=",len(arrY[x]))

# 打印表的名字和横纵轴的文字
plt.title("this cpu used", fontsize=24, color='#FF0000')
plt.xlabel("Time", fontsize=16)
plt.ylabel("CPU Used", fontsize=16)
plt.grid(True, color='g',linestyle='--',linewidth='1')
plt.ylim(0, 50)

# 绘制图形
for x in np.arange(len(name)):
	plt.plot(np.arange(0., arrCount[x], 1), arrY[x], c=cnames[x], label=name[x],)
plt.legend(loc='upper left')
plt.show()