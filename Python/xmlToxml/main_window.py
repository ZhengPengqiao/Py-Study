#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
import xml.sax
import xmlToxml
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMainWindow,QFileDialog,QLineEdit,QMessageBox
#重点和秘诀就在这里，大家注意看
from PyQt5.uic import loadUi


class main_window(QMainWindow):
	"""登录窗口"""
	def __init__(self, *args):
		super(main_window, self).__init__(*args)
		loadUi('main_window.ui', self)   #看到没，瞪大眼睛看		

	def getFileName(self): 
		file_name,  _ = QFileDialog.getOpenFileName(self, 'Open file', './')  
		self.lineEdit.setText(file_name)
		self.lineEdit_2.setText(file_name+".xml")

	def dealShaxToXml(self):
		# 创建一个 XMLReader
		parser = xml.sax.make_parser()
		# turn off namepsaces
		parser.setFeature(xml.sax.handler.feature_namespaces, 0)
	
		# 重写 ContextHandler
		Handler = xmlToxml.MovieHandler()
		parser.setContentHandler( Handler )
		parser.parse(self.lineEdit.text())
		Handler.showInfo()
		Handler.writeInfoToXml(self.lineEdit_2.text())
		QMessageBox.information(self, "提示", "转换并写入完成")
		