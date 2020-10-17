import math

from PyQt5.QtWidgets import (QWidget, QFrame, QLabel,
                             QGridLayout, QTextEdit)
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


class SdkInterface(QWidget):
    def __init__(self, window_size, dimention, AnswerArray = None):
        super().__init__()
        self.whsize = window_size
        self.dim = dimention
        self.root_dim = int(math.sqrt(self.dim))
        self.ans_array = AnswerArray

        self.initUI()
    
    def initUI(self):
        self.setFixedSize(self.whsize, self.whsize)
        self.layout = QGridLayout()
        self.nums_form = [[QLabel() for i in range(self.dim)] for j in range(self.dim)]
        for i in range(self.dim):
            for j in range(self.dim):
                numform = self.nums_form[i][j]
                # test!
                numform.setText(f"{self.ans_array[i][j]}")
                
                numform.setLineWidth(1)
                numform.setFrameStyle(QFrame.Box | QFrame.Plain)
                numform.setAlignment(Qt.AlignCenter)
                self.layout.addWidget(numform, i, j)
        
        self.layout.setHorizontalSpacing(1)
        self.layout.setVerticalSpacing(1)
        self.layout.setContentsMargins(1,1,1,1)

        self.setLayout(self.layout)
    
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        split = self.root_dim
        rect = self.rect()
        step = rect.width() / split
        PEN_WEIGHT = 3
        for i in range(0,split+1):
            painter.setPen(QPen(Qt.black, PEN_WEIGHT, Qt.SolidLine))
            x = step * i
            painter.drawLine(x,0,x,rect.height())
            painter.drawLine(0,x,rect.width(),x)

class SdkEditIF(SdkInterface):
    def initUI(self):
        self.setFixedSize(self.whsize, self.whsize)
        self.layout = QGridLayout()
        self.nums_form = [[QTextEdit() for i in range(self.dim)] for j in range(self.dim)]
        for i in range(self.dim):
            for j in range(self.dim):
                numform = self.nums_form[i][j]
                numform.setLineWidth(1)
                numform.setFrameStyle(QFrame.Box | QFrame.Plain)
                numform.setAlignment(Qt.AlignCenter)
                
                self.layout.addWidget(numform, i, j)
        
        self.layout.setHorizontalSpacing(1)
        self.layout.setVerticalSpacing(1)
        self.layout.setContentsMargins(1,1,1,1)

        self.setLayout(self.layout)
    
    def clearNums(self):
        for i in range(self.dim):
            for j in range(self.dim):
                self.nums_form[i][j].clear()
                self.nums_form[i][j].setAlignment(Qt.AlignCenter)
    
    def returnNumsArray(self):
        return self.nums_form