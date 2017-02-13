#-*- coding: UTF-8 -*-

from PyQt5 import QtWidgets
from MyFirstGui import Ui_MainWindow

class myWindow(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.new = Ui_MainWindow()
        self.new.setupUi(self)
        #将事件处理器与事件相连接
        self.new.pushButton.clicked.connect(self.button_clicked)

    #定义事件处理器
    def button_clicked(self):
        x = self.new.pushButton.x()
        y = self.new.pushButton.y()
        x += 50
        y += 50
        #点击时，移动按钮
        self.new.pushButton.move(x,y)

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = myWindow()
    myshow.show()
    sys.exit(app.exec_())