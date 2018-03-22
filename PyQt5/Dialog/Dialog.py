#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import MyDialog
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog

app = QApplication(sys.argv)
dlg = MyDialog.Ui_Dialog()
qtDlg = QDialog()
dlg.setupUi(qtDlg)
qtDlg.show()

exit(app.exec_())
