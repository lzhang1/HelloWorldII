#-*- coding: UTF-8 -*-

from PyQt5 import QtWidgets
from TempGui import Ui_MainWindow

class myWindow(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.new = Ui_MainWindow()
        self.new.setupUi(self)
        self.new.btnCtoF.clicked.connect(self.btnCtoF_Clicked)
        self.new.btnFtoC.clicked.connect(self.btnFtoC_Clicked)
        self.new.actionC_to_F.triggered.connect(self.btnCtoF_Clicked)
        self.new.actionF_to_C.triggered.connect(self.btnFtoC_Clicked)
        self.new.actionExit.triggered.connect(self.menuExit_selected)

    def btnCtoF_Clicked(self):
        cel = float(self.new.editCel.text())
        fahr = cel * 9.0 / 5 + 32
        self.new.spinFahr.setValue(int(fahr + 0.5))

    def btnFtoC_Clicked(self):
        fahr = self.new.spinFahr.value()
        cel = (fahr - 32) * 5 / 9.0
        cel_text = '%.2f'%cel
        self.new.editCel.setText(str(cel_text))

    def menuExit_selected(self):
        self.close()

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = myWindow()
    myshow.show()
    sys.exit(app.exec_())