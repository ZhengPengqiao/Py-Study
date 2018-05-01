#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
import random
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QListWidgetItem, QFileDialog
#重点和秘诀就在这里，大家注意看
from PyQt5.uic import loadUi
import MyMplCanvas
import numpy as np


class main_window(QMainWindow):
	"""登录窗口"""
	def __init__(self, *args):
		super(main_window, self).__init__(*args)
		loadUi('main_window.ui', self)   #看到没，瞪大眼睛看		
		self.test_mpl_canvas = MyMplCanvas.MyTestMplCanvas(self.centralwidget, width=5, height=4, dpi=100)
		if ( len(sys.argv) >= 2 ):
			self.test_mpl_canvas.file_name = sys.argv[1]
		self.action_Open.triggered.connect(self.show_getOpenFileName_dialog)  
		self.matplot_layout.addWidget(self.test_mpl_canvas)
		self.update_draw(self)

	# 按钮">"的点击时间,将选项添加到选中listWidget中
	def add_button_onClick(self, event):
		# 将选中的选项添加到显示选项,并从可选选项中移除
		item = self.listWidget_selects.currentItem()
		if( item == None):
			QMessageBox.information(self, "提示", "选项为空")
			return
		self.listWidget_selected.addItem(item.text())
		self.listWidget_selects.takeItem(self.listWidget_selects.row(item))


	# 按钮"<"的点击时间,将选中的选项移动到待选listWidget中
	def del_button_onClick(self, event):
		# 将选中的选项添加到可选选项,并从显示选项,中移除
		item = self.listWidget_selected.currentItem()
		if( item == None):
			QMessageBox.information(self, "提示", "选项为空")
			return
		self.listWidget_selects.addItem(item.text())
		self.listWidget_selected.takeItem(self.listWidget_selected.row(item))


	# 按钮">>"的点击时间,将选项添加到选中listWidget中
	def add_all_button_onClick(self, event):
		# 将选中的选项添加到显示选项,并从可选选项中移除
		for x in range( self.listWidget_selects.count()):
			item = self.listWidget_selects.takeItem(0)
			self.listWidget_selected.addItem(item.text())
		

	# 按钮"<<"的点击时间,将选中的选项移动到待选listWidget中
	def del_all_button_onClick(self, event):
		# 将选中的选项添加到可选选项,并从显示选项,中移除
		for x in range( self.listWidget_selected.count()):
			item = self.listWidget_selected.takeItem(0)
			self.listWidget_selects.addItem(item.text())

	def listWidget_selected_itemDoubleClicked(self, item):
		self.listWidget_selects.addItem(item.text())
		self.listWidget_selected.removeItemWidget(item)
		self.listWidget_selected.takeItem(self.listWidget_selected.row(item))

	def listWidget_selects_itemDoubleClicked(self, item):
		self.listWidget_selected.addItem(item.text())
		self.listWidget_selects.takeItem(self.listWidget_selects.row(item))

	def update_draw(self, event):
		# 将需要检查的数据记录到test_mpl_camvas类中的相应变量中
		self.test_mpl_canvas.color = []
		self.test_mpl_canvas.name = []
		for x in range( self.listWidget_selected.count()):
			self.test_mpl_canvas.name.append(self.listWidget_selected.item(x).text())
			colorrgb = [float(random.randint(0, 255))/float(255) for x in np.arange(3)]
			self.test_mpl_canvas.color.append(colorrgb)

		self.test_mpl_canvas.update_figure()


	def add_item_button_onClick(self, event):
		if self.lineEdit_itemString.text() == "":
			QMessageBox.information(self, "提示", "右侧编辑框为空,应先填写再添加")
			return
		self.listWidget_selects.addItem(self.lineEdit_itemString.text())
		self.lineEdit_itemString.setText("")


	def show_getOpenFileName_dialog(self):  
		file_name,  _ = QFileDialog.getOpenFileName(self, 'Open file', './')  
		self.test_mpl_canvas.file_name = file_name
		self.statusBar.showMessage("open file:"+self.test_mpl_canvas.file_name)
