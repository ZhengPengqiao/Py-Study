
import sys
import random

import matplotlib
matplotlib.use("Qt5Agg")
from PyQt5.QtWidgets import QSizePolicy, QWidget
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

#重点和秘诀就在这里，大家注意看

class MyMplCanvas(FigureCanvasQTAgg):
	"""这是一个窗口部件，即QWidget（当然也是FigureCanvasQTAgg）"""
	def __init__(self, parent=None, width=5, height=4, dpi=100):
		fig = Figure(figsize=(width, height), dpi=dpi)
		self.axes = fig.add_subplot(111)
		# 每次plot()调用的时候，我们希望原来的坐标轴被清除(所以False)
		self.axes.hold(False)

		FigureCanvasQTAgg.__init__(self, fig)
		self.setParent(parent)

		FigureCanvasQTAgg.setSizePolicy(self,
								QSizePolicy.Expanding,
								QSizePolicy.Expanding)
		FigureCanvasQTAgg.updateGeometry(self)



class MyTestMplCanvas(MyMplCanvas):
	"""动态画布：每秒自动更新，更换一条折线。"""
	def __init__(self, *args, **kwargs):
		self.file_name = ""
		self.color = []
		self.name = []
		
		MyMplCanvas.__init__(self, *args, **kwargs)


	def update_figure(self):
		print(">>>>>>>>>: ", self.name)
		print("<<<<<<<<<: ", self.color)
		self.update_canvas()
		self.draw()

	def update_canvas(self):

		if len(self.name) == 0:
			print("name count is 0, will return")
			return

		arr_count=[] * len(self.name)
		arrY= [[] for i in np.arange(len(self.name))]

		# 记录cpu,和进程名的位置
		cpu_index = -1
		name_index = -1

		# 读取文件中的数据
		with open(self.file_name, 'r') as f:
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
						for x in np.arange(len(self.name)):
							if (self.name[x] == item[-1]):
								arrY[x].append(float(item[cpu_index].replace("%","")))


		for x in np.arange(len(arrY)):
			print(self.name[x], "arrY[",x,"]=",len(arrY[x]), arrY[x])

		# 绘制图形
		for x in np.arange(len(self.name)):
			if ( x == 0):
				self.axes.hold(False)
				print(x , "===", False)
			else:
				self.axes.hold(True)
				print(x , "===", True)
			self.axes.plot(np.arange(0., len(arrY[x]), 1), arrY[x], c=self.color[x], label=self.name[x],)
		self.axes.legend(loc='center left')

		# 打印表的名字和横纵轴的文字
		self.axes.set_xlabel("Time", fontsize=16)
		self.axes.set_ylabel("CPU Used", fontsize=16)
		self.axes.grid(True, color='g',linestyle='--',linewidth='1')
		self.axes.set_ylim(0, 100)

		# 标记一条刻度线
		# plt.axhline(y=18, xmin=0, xmax=100, c='#FFFF00')
		self.axes.set_yticks(np.arange(0, 101, 2))

