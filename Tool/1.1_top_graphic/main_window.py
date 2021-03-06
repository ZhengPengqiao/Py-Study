#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
import random
from PyQt5.QtCore import QCoreApplication 
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QListWidgetItem, QFileDialog
from PyQt5.QtGui import QPixmap, QGuiApplication  
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
		self.actionSave_windows.triggered.connect(self.save_windows)
		self.action_show_step_sub5.triggered.connect(self.show_step_sub5)
		self.action_show_step_add5.triggered.connect(self.show_step_add5)

		self.matplot_layout.addWidget(self.test_mpl_canvas)
		self.update_draw(self)

	# 按钮">"的点击时间,将选项添加到选中listWidget中
	def add_button_onClick(self, event):
		self.test_mpl_canvas.is_usrselectname=1
		# 将选中的选项添加到显示选项,并从可选选项中移除
		item = self.listWidget_selects.currentItem()
		if( item == None):
			QMessageBox.information(self, "提示", "选项为空")
			return
		self.listWidget_selected.addItem(item.text())
		self.listWidget_selects.takeItem(self.listWidget_selects.row(item))


	# 按钮"<"的点击时间,将选中的选项移动到待选listWidget中
	def del_button_onClick(self, event):
		self.test_mpl_canvas.is_usrselectname=1
		# 将选中的选项添加到可选选项,并从显示选项,中移除
		item = self.listWidget_selected.currentItem()
		if( item == None):
			QMessageBox.information(self, "提示", "选项为空")
			return
		self.listWidget_selects.addItem(item.text())
		self.listWidget_selected.takeItem(self.listWidget_selected.row(item))


	# 按钮">>"的点击时间,将选项添加到选中listWidget中
	def add_all_button_onClick(self, event):
		self.test_mpl_canvas.is_usrselectname=1
		# 将选中的选项添加到显示选项,并从可选选项中移除
		for x in range( self.listWidget_selects.count()):
			item = self.listWidget_selects.takeItem(0)
			self.listWidget_selected.addItem(item.text())
		

	# 按钮"<<"的点击时间,将选中的选项移动到待选listWidget中
	def del_all_button_onClick(self, event):
		self.test_mpl_canvas.is_usrselectname=1
		# 将选中的选项添加到可选选项,并从显示选项,中移除
		for x in range( self.listWidget_selected.count()):
			item = self.listWidget_selected.takeItem(0)
			self.listWidget_selects.addItem(item.text())


	def listWidget_selected_itemDoubleClicked(self, item):
		self.test_mpl_canvas.is_usrselectname=1
		self.listWidget_selects.addItem(item.text())
		self.listWidget_selected.removeItemWidget(item)
		self.listWidget_selected.takeItem(self.listWidget_selected.row(item))

	def listWidget_selects_itemDoubleClicked(self, item):
		self.test_mpl_canvas.is_usrselectname=1
		self.listWidget_selected.addItem(item.text())
		self.listWidget_selects.takeItem(self.listWidget_selects.row(item))

	def update_draw(self, event):
		# 将需要检查的数据记录到test_mpl_camvas类中的相应变量中
		self.test_mpl_canvas.limit_yl = int(self.lineEdit_YL.text().strip())
		self.test_mpl_canvas.limit_yh = int(self.lineEdit_YH.text().strip())
		self.test_mpl_canvas.color = []
		self.test_mpl_canvas.name = []
		self.test_mpl_canvas.loc_str = self.loc_pos.currentText()
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
		self.test_mpl_canvas.is_usrselectname=0
		self.test_mpl_canvas.color.clear()
		self.test_mpl_canvas.name.clear()
		self.listWidget_selects.clear()
		self.listWidget_selected.clear()
		self.test_mpl_canvas.update_figure()
		for x in range( len(self.test_mpl_canvas.name) ):
			print(self.test_mpl_canvas.name[x])
			self.listWidget_selected.addItem(self.test_mpl_canvas.name[x])
		self.test_mpl_canvas.is_usrselectname=1


	def show_step_add5(self):
		self.test_mpl_canvas.step+=5
		self.update_draw(self)

	def show_step_sub5(self):
		self.test_mpl_canvas.step-=5
		if( self.test_mpl_canvas.step < 1 ):
			self.test_mpl_canvas.step=1
		self.update_draw(self)

	def save_windows(self):
		screen = QGuiApplication.primaryScreen();
		originalPixmap = screen.grabWindow(0)
		originalPixmap.save('windows.png','png')