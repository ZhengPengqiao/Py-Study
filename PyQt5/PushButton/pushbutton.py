#!/usr/bin/python3
# -*- coding:utf-8 -*-

'''
PushButton
'''
import sys

# 这里我们提供必要的引用, 基本控件位于PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QPushButton

# 每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建QPushButton控件
    pushButton = QPushButton()
    # 设置窗口位置及大小
    pushButton.setGeometry(100, 100, 100, 100)
    # 设置窗口标题
    pushButton.setWindowTitle('pushButton')
    # 设置pushButton的文本
    pushButton.setText("Close")
    # 将pushButton显示出来
    pushButton.show()

    # 系统exit()方法确保应用程序干净的退出
    # 的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
    sys.exit(app.exec_())
