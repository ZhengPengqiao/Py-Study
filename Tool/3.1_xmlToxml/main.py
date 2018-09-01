#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-


import sys

from PyQt5.QtWidgets import QApplication
import main_window

if __name__ == '__main__':
			
	app = QApplication(sys.argv)
	window = main_window.main_window()
	window.show()
    
	sys.exit(app.exec_())
