# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TempGui.ui'
#
# Created: Fri Feb 10 18:57:44 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnCtoF = QtWidgets.QPushButton(self.centralwidget)
        self.btnCtoF.setGeometry(QtCore.QRect(290, 130, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnCtoF.setFont(font)
        self.btnCtoF.setIconSize(QtCore.QSize(16, 16))
        self.btnCtoF.setObjectName("btnCtoF")
        self.btnFtoC = QtWidgets.QPushButton(self.centralwidget)
        self.btnFtoC.setGeometry(QtCore.QRect(290, 280, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnFtoC.setFont(font)
        self.btnFtoC.setIconSize(QtCore.QSize(16, 16))
        self.btnFtoC.setObjectName("btnFtoC")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 250, 54, 12))
        self.label.setObjectName("label")
        self.editCel = QtWidgets.QLineEdit(self.centralwidget)
        self.editCel.setGeometry(QtCore.QRect(112, 220, 81, 20))
        self.editCel.setObjectName("editCel")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(560, 250, 54, 12))
        self.label_2.setObjectName("label_2")
        self.spinFahr = QtWidgets.QSpinBox(self.centralwidget)
        self.spinFahr.setGeometry(QtCore.QRect(561, 220, 51, 22))
        self.spinFahr.setMinimum(-460)
        self.spinFahr.setMaximum(1000000)
        self.spinFahr.setObjectName("spinFahr")
        # MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuConvert = QtWidgets.QMenu(self.menubar)
        self.menuConvert.setObjectName("menuConvert")
        # MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)
        self.actionC_to_F = QtWidgets.QAction(MainWindow)
        self.actionC_to_F.setObjectName("actionC_to_F")
        self.actionFotC = QtWidgets.QAction(MainWindow)
        self.actionFotC.setObjectName("actionFotC")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionF_to_C = QtWidgets.QAction(MainWindow)
        self.actionF_to_C.setObjectName("actionF_to_C")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuConvert.addSeparator()
        self.menuConvert.addAction(self.actionC_to_F)
        self.menuConvert.addAction(self.actionF_to_C)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuConvert.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnCtoF.setText(_translate("MainWindow", "Celsius to Fahrenheit >>>"))
        self.btnFtoC.setText(_translate("MainWindow", "<<< Fahrenheit to Celsius"))
        self.label.setText(_translate("MainWindow", "Celsius"))
        self.label_2.setText(_translate("MainWindow", "Fahrenheit"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuConvert.setTitle(_translate("MainWindow", "&Convert"))
        self.actionC_to_F.setText(_translate("MainWindow", "&C to F"))
        self.actionFotC.setText(_translate("MainWindow", "FotC"))
        self.actionExit.setText(_translate("MainWindow", "&Exit"))
        self.actionF_to_C.setText(_translate("MainWindow", "&F to C"))

