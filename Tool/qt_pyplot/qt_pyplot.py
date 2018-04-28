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
		self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')

	def update_figure(self):
		# 构建4个随机整数，位于闭区间[0, 10]
		l = [random.randint(0, 10) for i in np.arange(4)]
		self.axes.plot([0, 1, 2, 3], l, 'r')
		self.draw()

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
