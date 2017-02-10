# -*- coding: UTF-8 -*-

# from PyQt5 import QtWidgets
# from first import Ui_MainWindow
#
# class myWindow(QtWidgets.QWidget, Ui_MainWindow):
#     def __init__(self):
#         super(myWindow, self).__init__()
#         self.new = Ui_MainWindow()
#         self.new.setupUi(self)
#
# if __name__=="__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     myshow = myWindow()
#     myshow.show()
#     sys.exit(app.exec_())

# import sys
#
# from PyQt5.QtWidgets import QApplication , QMainWindow
#
# from firstPyQt5 import *
#
# if __name__ == '__main__':
#     '''
#     主函数
#     '''

    # app = QApplication(sys.argv)
    # mainWindow = QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(mainWindow)
    # mainWindow.show()
    # sys.exit(app.exec_())

from PyQt5 import *
from firstPyQt5 import *
import sys

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    ui=Ui_MainWindow()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())