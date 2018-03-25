#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
import MyUI
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
my = MyUI.UI_Widget()
sys.exit(app.exec_())
