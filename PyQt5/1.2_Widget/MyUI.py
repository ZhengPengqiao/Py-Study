#!/usr/bin/python3
# -*- coding:utf-8 -*-

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('bear.png'))
        self.show()
