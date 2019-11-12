
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
		self.limit_yl = 0
		self.limit_yh = 100
		self.step = 5
		self.loc_str = 'top right'
		self.is_usrselectname = 0
		
		MyMplCanvas.__init__(self, *args, **kwargs)


	def update_figure(self):
		print(">>>>>>>>>: ", self.name)
		print("<<<<<<<<<: ", self.color)
		self.update_canvas()
		self.draw()

	def update_canvas(self):

		print(self.file_name)
		if ( len(self.file_name) == 0 ):
			print("self.file_name is empty")
			return

		index=0
		arrY= [[] for i in np.arange(20)]
		# 读取文件中的数据
		with open(self.file_name, 'r') as f:
			linea = f.readlines()

			for x in np.arange(len(linea)):
				if( self.is_usrselectname != 1 ):
					print("deal all line:")
					# 解析用户占用和系统占用的资源
					item = linea[x].split(",") 	#每一行中的每个信息，第一个是名字，后面是数据值
					self.name.append(item[0])
					colorrgb = [float(random.randint(0, 255))/float(255) for x in np.arange(3)]
					self.color.append(colorrgb)
					for i in np.arange(len(item)-1):
						tmp_val = float(item[i+1].replace("%",""))
						arrY[x].append(tmp_val)
					index=index+1
					
				else:
					# 解析用户占用和系统占用的资源
					item = linea[x].split(",") 	#每一行中的每个信息，第一个是名字，后面是数据值
					if ( item[0] in self.name ):
						print("deal select item:" + item[0])
						for i in np.arange(len(item)-1):
							tmp_val = float(item[i+1].replace("%",""))
							arrY[index].append(tmp_val)
						index=index+1
					else:
						print("ignore no select item:" + item[0])

		for x in np.arange(len(self.name)):
			print(self.name[x], "arrY[",x,"]=",len(arrY[x]), arrY[x])

		print("limit y l->h loc_pos", self.limit_yl, self.limit_yh, self.loc_str);

		# 绘制图形
		for x in np.arange(len(self.name)):
			if ( x == 0):
				self.axes.hold(False)
				print(x , "===", False)
			else:
				self.axes.hold(True)
				print(x , "===", True)
			self.axes.plot(np.arange(0., len(arrY[x]), 1), arrY[x], c=self.color[x], label=self.name[x],)
		self.axes.legend(loc=self.loc_str)

		# 打印表的名字和横纵轴的文字
		self.axes.set_xlabel("Time", fontsize=16)
		self.axes.set_ylabel("Val", fontsize=16)
		self.axes.grid(True, color='g',linestyle='--',linewidth='1')
		self.axes.set_ylim(self.limit_yl, self.limit_yh)

		# 标记一条刻度线
		# plt.axhline(y=18, xmin=0, xmax=100, c='#FFFF00')
		self.axes.set_yticks(np.arange(self.limit_yl, self.limit_yh, self.step))

