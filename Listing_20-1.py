# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets

class MyWindowClass(QtWidgets.QWidget):
    def __init__(self):
        super(MyWindowClass,self).__init__()

app = QtWidgets.QApplication(sys.argv)
myWindow = MyWindowClass()
myWindow.resize(250,150)
myWindow.setWindowTitle('example')
myWindow.show()
sys.exit(app.exec_())

