##一, 利用designer设计的GUI
1.1 使用designer设计一个简单的GUI界面，含有一个'Quit'按钮
1.2 把MyFirstGui.ui文件转成MyFirstGui.py文件
1.3 修改MyFirstGui.py文件
1.4 创建文件调用MyFirstGui.py

````
from PyQt5 import QtWidgets
from MyFirstGui import Ui_MainWindow

class myWindow(QtWidgets.QWidget, Ui_MainWindow):
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
````

##二， 创建点击事件
2.1 修改文件
````
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
````

##三, 创建一个温度转换窗口
3.1 利用designer设计界面TempGui.ui
3.2 把TempGui.ui文件转成TempGui.py文件
3.3 修改TempGui.py文件
3.4 创建文件调用TempGui.py


##四， 创建带菜单窗口

##五， 创建热键