# -*- coding: utf-8 -*-

import sys
import cv2
import numpy as np
from PIL import Image
import scipy
import deep_mnist
import mnist_recognizer

from widget_painted import *
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from scipy import ndimage

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

width = 1200
height = 200
paint_width = 360
paint_height = 360
mnist_width = 28
mnist_height = 28
mnist_size = (mnist_width, mnist_height)

# 16*16近傍の定義
kernel = np.ones((16, 16), np.uint8)

class MainWindow(QtGui.QMainWindow, deep_mnist.Ui_MainWindow):
    def __init__(self):
        super(self. __class__, self).__init__()
        self.setupUi(self)
        self.move(width,height)
        self.textEdit.setText("Deep MNIST for Experts")
        self.image = np.zeros((paint_width, paint_height,3), np.uint8)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        self.mnist_image = np.zeros((mnist_width, mnist_height,3), np.uint8)
        self.mnist_image = cv2.cvtColor(self.mnist_image, cv2.COLOR_RGB2GRAY)

    def paint_image(self):
        self.textEdit.append("open paint window...")
        view_paint.show()

        # TODO:Input画像(28*28)を表示
        # view_result.show()

    def saved(self):
        self.textEdit.append("saving...")

        for point in view_paint.points_saved:
            self.image[point.x(), point.y()] = 255

        # 上下反転
        self.image = cv2.flip(self.image, 0)
        # 時計回り回転
        self.image = ndimage.rotate(self.image, 270)
        # cv2.imwrite("out_put.bmp", self.image)
        # 膨張処理
        image_dilation = cv2.dilate(self.image, kernel, iterations = 1)
        cv2.imwrite("dilation.bmp", image_dilation)
        # 縮小処理
        self.mnist_image = cv2.resize(image_dilation, mnist_size)
        cv2.imwrite("mnist.bmp", self.mnist_image)
        # 2値化で強調、BINARY_INVで反転し、白背景で黒文字にする
        ret,thre_image = cv2.threshold(self.mnist_image, 5, 255, cv2.THRESH_BINARY_INV)
        cv2.imwrite("thre_image.bmp",thre_image)

        self.textEdit.append("finished to save...")

    def recognize_number(self):
        self.textEdit.append("saving...")

        for point in view_paint.points_saved:
            self.image[point.x(), point.y()] = 255

        # 上下反転
        self.image = cv2.flip(self.image, 0)
        # 時計回り回転
        self.image = ndimage.rotate(self.image, 270)
        # cv2.imwrite("out_put.bmp", self.image)
        # 膨張処理
        image_dilation = cv2.dilate(self.image, kernel, iterations = 1)
        cv2.imwrite("dilation.bmp", image_dilation)
        # 縮小処理
        self.mnist_image = cv2.resize(image_dilation, mnist_size)
        cv2.imwrite("mnist.bmp", self.mnist_image)
        # 2値化で強調、BINARY_INVで反転し、白背景で黒文字にする
        ret,thre_image = cv2.threshold(self.mnist_image, 5, 255, cv2.THRESH_BINARY_INV)
        cv2.imwrite("thre_image.bmp",thre_image)

        self.textEdit.append("finished to save...")

        self.textEdit.append("recognize...")
        self.textEdit.append("result=")

        result = mnist_recognizer.mnist_recognizer(thre_image)
        self.textEdit.append(str(result))

        # スクロールを下に移動
        self.textEdit.verticalScrollBar().triggerAction(QtGui.QAbstractSlider.SliderToMaximum)

        self.image = np.zeros((paint_width, paint_height,3), np.uint8)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        self.mnist_image = np.zeros((mnist_width, mnist_height,3), np.uint8)
        self.mnist_image = cv2.cvtColor(self.mnist_image, cv2.COLOR_RGB2GRAY)

    def clear_points(self):
        self.textEdit.append("clear image...")
        view_paint.close()
        view_paint.__init__()
        view_paint.move(width,height+500)
        view_paint.setWindowTitle(_translate("", "①数字を書く", None))
        view_paint.setFixedSize(QSize(360,360))
        view_paint.show()

        self.image = np.zeros((paint_width, paint_height,3), np.uint8)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        self.mnist_image = np.zeros((mnist_width, mnist_height,3), np.uint8)
        self.mnist_image = cv2.cvtColor(self.mnist_image, cv2.COLOR_RGB2GRAY)

        self.textEdit.verticalScrollBar().triggerAction(QtGui.QAbstractSlider.SliderToMaximum)

    def  quit(self):
        print "close..."
        mnist_recognizer.close()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    view_paint = PaintedWidget()
    view_paint.move(width,height+500)
    view_paint.setWindowTitle(_translate("", "①数字を書く", None))
    view_paint.setFixedSize(QSize(360,360))
    view_result = QWidget()
    view_result.move(width+360,height+500)
    view_result.setWindowTitle(_translate("", "MNIST用画像に変換", None))
    view_result.setFixedSize(QSize(mnist_width,mnist_height))

    form.pushButtonPaintImage.clicked.connect(lambda: form.paint_image())
    form.pushButtonSaveImage.clicked.connect(lambda: form.saved())
    form.pushButtonRecognizeNumber.clicked.connect(lambda: form.recognize_number())
    form.pushButtonClear.clicked.connect(lambda: form.clear_points())
    form.button_exit.clicked.connect(app.quit)
    form.button_exit.clicked.connect(lambda: form.quit())

    app.exec_()
