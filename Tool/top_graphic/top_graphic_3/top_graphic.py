#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-


import sys
import random

import matplotlib
matplotlib.use("Qt5Agg")

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton

import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MyMplCanvas(FigureCanvasQTAgg):
	"""这是一个窗口部件，即QWidget（当然也是FigureCanvasQTAgg）"""
	def __init__(self, parent=None, width=5, height=4, dpi=100):
		fig = Figure(figsize=(width, height), dpi=dpi)
		self.axes = fig.add_subplot(111)
		# 每次plot()调用的时候，我们希望原来的坐标轴被清除(所以False)
		self.axes.hold(False)

		self.compute_initial_figure()

		#
		FigureCanvasQTAgg.__init__(self, fig)
		self.setParent(parent)

		FigureCanvasQTAgg.setSizePolicy(self,
								QSizePolicy.Expanding,
								QSizePolicy.Expanding)
		FigureCanvasQTAgg.updateGeometry(self)

	def compute_initial_figure(self):
		pass

class MyTestMplCanvas(MyMplCanvas):
	"""动态画布：每秒自动更新，更换一条折线。"""
	def __init__(self, *args, **kwargs):
		MyMplCanvas.__init__(self, *args, **kwargs)

	def compute_initial_figure(self):
		self.update_canvas()

	def update_figure(self):
		self.update_canvas()
		self.draw()

	def update_canvas(self):
		if len(sys.argv) < 2:
			print("Used: ", sys.argv[0], " file_name")
			sys.exit()

		file_name = sys.argv[1]

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

		# 绘制图形
		for x in np.arange(len(name)):
			if ( x == 0):
				self.axes.hold(False)
			else:
				self.axes.hold(True)
			self.axes.plot(np.arange(0., len(arrY[x]), 1), arrY[x], c=color[x], label=name[x],)
		self.axes.legend(loc='center left')

		# 打印表的名字和横纵轴的文字
		self.axes.set_title("this cpu used", fontsize=24, color='#FF0000')
		self.axes.set_xlabel("Time", fontsize=16)
		self.axes.set_ylabel("CPU Used", fontsize=16)
		self.axes.grid(True, color='g',linestyle='--',linewidth='1')
		self.axes.set_ylim(0, 100)

		# 标记一条刻度线
		# plt.axhline(y=18, xmin=0, xmax=100, c='#FFFF00')
		self.axes.set_yticks(np.arange(0, 101, 2))


class ApplicationWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		self.setWindowTitle("程序主窗口")

		self.file_menu = QMenu('&File', self)
		self.file_menu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
		self.menuBar().addMenu(self.file_menu)

		self.help_menu = QMenu('&Help', self)
		self.menuBar().addSeparator()
		self.menuBar().addMenu(self.help_menu)

		self.help_menu.addAction('&About', self.about)

		self.main_widget = QWidget(self)

		layout = QVBoxLayout(self.main_widget)
		test_mpl_canvas = MyTestMplCanvas(self.main_widget, width=5, height=4, dpi=100)

		pushButton = QPushButton(self.main_widget)
		pushButton.setText("Change Canvas")
		pushButton.clicked.connect(test_mpl_canvas.update_figure)

		layout.addWidget(pushButton)
		layout.addWidget(test_mpl_canvas)

		self.main_widget.setFocus()
		self.setCentralWidget(self.main_widget)
		# 状态条显示2秒
		self.statusBar().showMessage("将matplotlib窗口绘制在qt中 !", 2000)

	def fileQuit(self):
		self.close()

	def closeEvent(self, ce):
		self.fileQuit()

	def about(self):
		QMessageBox.about(self, "About",
		"""embedding_in_qt5.py example
		Copyright 2015 BoxControL

		This program is a simple example of a Qt5 application embedding matplotlib
		canvases. It is base on example from matplolib documentation, and initially was
		developed from Florent Rougon and Darren Dale.

		http://matplotlib.org/examples/user_interfaces/embedding_in_qt4.html

		It may be used and modified with no restriction; raw copies as well as
		modified versions may be distributed without limitation.
		"""
		)

if __name__ == '__main__':
	
	app = QApplication(sys.argv)

	aw = ApplicationWindow()
	aw.setWindowTitle("PyQt5 与 Matplotlib 例子")
	aw.show()
	sys.exit(app.exec_())
