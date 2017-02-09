# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
import MyFirstGui


class MyWindowClass(QtWidgets.QWidget, MyFirstGui):
    def __init__(self, parent=None):
        super(MyWindowClass,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        x = self.pushButton.x()
        y = self.pushButton.y()
        x += 50
        y += 50
        self.pushButton.move(x, y)     # Move the button when we click it

app = QtWidgets.QApplication(sys.argv)
myWindow = MyWindowClass()
label=QtWidgets.QLabel(myWindow)
label.setText("hello world")
myWindow.resize(640,480)
myWindow.show()
sys.exit(app.exec_())
