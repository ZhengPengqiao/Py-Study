#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QMessageBox
#重点和秘诀就在这里，大家注意看
from PyQt5.uic import loadUi

class Login(QMainWindow):
    """登录窗口"""
    def __init__(self, *args):
        super(Login, self).__init__(*args)
        loadUi('Login.ui', self)   #看到没，瞪大眼睛看
        
        # 可以在ui文件中设置,也可以在这里使用代码进行链接
        # self.button_show.clicked.connect(self.button_show_text)
        # self.button_reset.clicked.connect(self.button_clear_text)
        # self.button_quit.clicked.connect(QCoreApplication.instance().quit)

    def button_show_text(self, event):
        QMessageBox.information(self, 'Show Message', self.lineEdit_name.text() + " " + self.lineEdit_age.text())

    def button_clear_text(self, event):
        self.lineEdit_age.setText("")    
        self.lineEdit_name.setText("")    
