#!/usr/bin/python3
# -*- coding:utf-8 -*-

'''
QWidget
'''

import sys

# 引用必要控件
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
    app = QApplication(sys.argv)

    # 创建QWidget对象
    w = QWidget()
    # 设置大小
    w.resize(250, 250)
    # 设置位置
    w.move(300, 300)
    # 设置窗口标题
    w.setWindowTitle('QWidget')
    # 显示窗口
    w.show()

    sys.exit(app.exec_())
