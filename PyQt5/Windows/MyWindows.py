#!/usr/bin/python3
# -*- coding:utf-8 -*-

# QtGui,QDesktopWidget类提供了用户的桌面信息,包括屏幕大小
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QMessageBox)
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QLabel, QLineEdit, QTextEdit
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout
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


class Windows_AbsoltueWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        lbl1 = QLabel('Label1', self)
        lbl1.move(15, 10)

        lbl2 = QLabel('Label2', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('Label3', self)
        lbl3.move(55, 70)

        lbl4 = QLabel('Label3', self)
        lbl4.move(75, 100)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')
        self.show()


class Windows_BoxlayoutWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        button1_1 = QPushButton("button1_1")
        button1_1.clicked.connect(self.btn_clicked)
        button1_2 = QPushButton("button1_2")
        button1_2.clicked.connect(self.btn_clicked)
        button2_1 = QPushButton("button2_1")
        button2_1.clicked.connect(self.btn_clicked)
        button2_2 = QPushButton("button2_2")
        button2_2.clicked.connect(self.btn_clicked)

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(button1_1)
        hbox1.addWidget(button1_2)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(button2_1)
        hbox2.addWidget(button2_2)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()

    def btn_clicked(self, event):
        QMessageBox.information(self, 'Btn_clicked', 'You Click Buttom')


class Windows_GridLayoutWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()


class Windows_GridLayout1Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()
