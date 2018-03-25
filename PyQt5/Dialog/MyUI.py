#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog


class MyDialog(QDialog):
    'this a my dialog with two button'

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("Dialog")
        self.resize(640, 480)
        buttonBox = QtWidgets.QDialogButtonBox(self)
        buttonBox.setOrientation(QtCore.Qt.Horizontal)
        buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        buttonBox.setObjectName("buttonBox")
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        QtCore.QMetaObject.connectSlotsByName(self)

        self.setGeometry(400, 400, 600, 400)
        self.move(100, 100)
        self.setWindowTitle('Ui_Dialog')
        self.show()
