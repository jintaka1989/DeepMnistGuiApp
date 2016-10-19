   # Copyright 2016 Satoshi TAKAGI <jintaka198912@gmail.com>
   #
   # Licensed under the Apache License, Version 2.0 (the "License");
   # you may not use this file except in compliance with the License.
   # You may obtain a copy of the License at
   #
   #     http://www.apache.org/licenses/LICENSE-2.0
   #
   # Unless required by applicable law or agreed to in writing, software
   # distributed under the License is distributed on an "AS IS" BASIS,
   # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   # See the License for the specific language governing permissions and
   # limitations under the License.

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
