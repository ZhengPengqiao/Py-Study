#!/usr/bin/python3
# -*- coding:utf-8 -*-

from PyQt5.QtWidgets import QApplication, QAction, QFileDialog,  QTextEdit  , QPushButton
from PyQt5 import QtWidgets  
from PyQt5.QtCore import Qt  
from PyQt5.QtGui import QIcon  

class OpenFile(QtWidgets.QMainWindow):  
	def __init__(self, parent= None):  
		QtWidgets.QWidget.__init__(self)  

		self.setGeometry(300, 300, 150, 110)  
		self.setWindowTitle('OpenFile')  
		self.textEdit = QTextEdit()  
		self.setCentralWidget(self.textEdit)  

		self.statusBar()  
		self.setFocus()


		exit = QAction(QIcon('icons/Blue_Flower.ico'), 'Open', self)  
		exit.setShortcut('Ctrl+O')  
		exit.setStatusTip('Open new file')  

		exit.triggered.connect(self.showDialog)  

		menubar = self.menuBar()  
		file = menubar.addMenu('&File')  
		file.addAction(exit)

		self.open_button = QPushButton("Open", self)
		self.open_button.move(0, 0)
		self.open_button.clicked.connect(self.open_button_onClocked)

	def open_button_onClocked(self, event):
		filename,  _ = QFileDialog.getOpenFileName(self, 'Open file', './')  
		if filename:  
			file = open(filename)  
			data = file.read()   
			self.textEdit.setText(data)  
  

	def showDialog(self):  
		filename,  _ = QFileDialog.getOpenFileName(self, 'Open file', './')  
		if filename:  
			file = open(filename)  
			data = file.read()   
			self.textEdit.setText(data)  
  
if __name__ == "__main__":  
	import sys  
	app = QApplication(sys.argv)  
	qb = OpenFile()  
	qb.show()  
	sys.exit(app.exec_())