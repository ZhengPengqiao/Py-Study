#!/usr/bin/python3
# -*- coding:utf-8 -*-

# QtGui,QDesktopWidget类提供了用户的桌面信息,包括屏幕大小
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QMessageBox)
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication


class Windows_Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 这种静态的方法设置一个用于显示工具工具提示的字体
        QToolTip.setFont(QFont('SansSerif', 10))

        # 创建一个提示,我们称之为settooltip()方法,我们可以使用丰富的文本格式
        self.setToolTip('this is a <b>QWidget</b> widget')

        # 创建一个PushButton并为它设置tooptip
        btn = QPushButton('Button', self)
        btn.clicked.connect(self.btn_clocked)
        btn.setToolTip('This is a </b>QPushButton </b> widget')
        btn.resize(100, 100)
        btn.move(50, 50)

        quit = QPushButton("Quit", self)
        quit.move(10, 10)
        quit.clicked.connect(QCoreApplication.instance().quit)

        self.setGeometry(400, 400, 600, 400)
        self.setWindowTitle('Tooptip')
        self.center()
        self.show()

    # 控制窗口显示在屏幕中心的方法
    def center(self):
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def btn_clocked(self, event):
        QMessageBox.information(self, 'Message', "You Click Button")

    # 在窗口退出的到时候,弹出对话框,询问是否退出
    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
