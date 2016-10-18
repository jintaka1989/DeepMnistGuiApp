import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import cv2
import numpy
import pdb
import scipy

class PaintedWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.px = None
        self.py = None
        self.points = []
        self.psets = []
        self.points_saved = []

    def mousePressEvent(self, event):
        self.points.append(event.pos())
        self.update()

    def mouseMoveEvent(self, event):
        self.points.append(event.pos())
        self.update()

    def mouseReleaseEvent(self, event):
        self.pressed = False
        self.psets.append(self.points)
        self.points_saved.extend(self.points)
        self.points = []
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.white)
        painter.drawRect(self.rect())

        painter.setPen(Qt.black)

        # draw historical points
        for points in self.psets:
            painter.drawPolyline(*points)

        # draw current points
        if self.points:
            painter.drawPolyline(*self.points)
