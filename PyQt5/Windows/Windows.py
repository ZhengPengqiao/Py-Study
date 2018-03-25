#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
import MyWindows
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
my1 = MyWindows.Windows_GridLayout1Window()
sys.exit(app.exec_())
