# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deep_mnist.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.button_exit = QtGui.QPushButton(self.centralwidget)
        self.button_exit.setGeometry(QtCore.QRect(450, 390, 181, 27))
        self.button_exit.setObjectName(_fromUtf8("button_exit"))
        self.pushButtonPaintImage = QtGui.QPushButton(self.centralwidget)
        self.pushButtonPaintImage.setGeometry(QtCore.QRect(450, 170, 181, 27))
        self.pushButtonPaintImage.setObjectName(_fromUtf8("pushButtonPaintImage"))
        self.pushButtonSaveImage = QtGui.QPushButton(self.centralwidget)
        self.pushButtonSaveImage.setGeometry(QtCore.QRect(450, 360, 181, 27))
        self.pushButtonSaveImage.setObjectName(_fromUtf8("pushButtonSaveImage"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 30, 421, 391))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(520, 30, 81, 131))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.pushButtonClear = QtGui.QPushButton(self.centralwidget)
        self.pushButtonClear.setGeometry(QtCore.QRect(450, 270, 181, 27))
        self.pushButtonClear.setObjectName(_fromUtf8("pushButtonClear"))
        self.pushButtonRecognizeNumber = QtGui.QPushButton(self.centralwidget)
        self.pushButtonRecognizeNumber.setGeometry(QtCore.QRect(450, 240, 181, 27))
        self.pushButtonRecognizeNumber.setObjectName(_fromUtf8("pushButtonRecognizeNumber"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.button_exit.setText(_translate("MainWindow", "アプリを終了する", None))
        self.pushButtonPaintImage.setText(_translate("MainWindow", "描画画面を起動", None))
        self.pushButtonSaveImage.setText(_translate("MainWindow", "描画画面を保存する", None))
        self.pushButtonClear.setText(_translate("MainWindow", "③描画をクリアする", None))
        self.pushButtonRecognizeNumber.setText(_translate("MainWindow", "②数字を認識する", None))

