#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import MyUI
import sys
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
my = MyUI.MyDialog()

exit(app.exec_())
