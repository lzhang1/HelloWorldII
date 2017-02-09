# -*- coding: UTF-8 -*-

from PyQt5 import QtWidgets
from uiform import Ui_MainWindow

class myWindow(QtWidgets.QWidget):
    def __init__(self):
        super(myWindow, self).__init__()
        self.new = Ui_MainWindow()
        self.new.setupUi(self)

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = myWindow()
    myshow.show()
    sys.exit(app.exec_())