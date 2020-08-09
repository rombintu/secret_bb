# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'building_secret.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(273, 534)
        MainWindow.setMinimumSize(QtCore.QSize(273, 534))
        MainWindow.setMaximumSize(QtCore.QSize(273, 534))
        MainWindow.setAcceptDrops(True)
        MainWindow.setStyleSheet("*{\n"
"    background-color: rgb(221, 250, 255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 231, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 228, 164);")
        self.lineEdit.setInputMask("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 10, 151, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 90, 131, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 170, 131, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 250, 131, 21))
        self.label_4.setObjectName("label_4")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(20, 360, 231, 41))
        self.textBrowser_4.setStyleSheet("background-color: rgb(255, 228, 164);\n"
"")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 330, 131, 21))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 430, 71, 41))
        self.pushButton.setStyleSheet("background-color: rgb(255, 228, 164);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 480, 161, 21))
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 120, 231, 41))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 228, 164);")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 200, 231, 41))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 228, 164);")
        self.lineEdit_3.setInputMask("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 280, 231, 41))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 228, 164);")
        self.lineEdit_4.setInputMask("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Building Secret"))
        self.label.setText(_translate("MainWindow", "Enter sh-gramm"))
        self.label_2.setText(_translate("MainWindow", "Gamma - 1"))
        self.label_3.setText(_translate("MainWindow", "Gamma - 2"))
        self.label_4.setText(_translate("MainWindow", "Gamma - 3"))
        self.label_5.setText(_translate("MainWindow", "Secret"))
        self.pushButton.setText(_translate("MainWindow", "Go"))
        self.label_6.setText(_translate("MainWindow", "by Nicolsky"))
