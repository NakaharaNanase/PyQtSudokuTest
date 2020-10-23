import math

from PyQt5.QtWidgets import (QWidget, QFrame, QLabel,
                             QGridLayout, QTextEdit)
from PyQt5.QtGui import QPainter, QColor, QPen, QFont
from PyQt5.QtCore import Qt


class SdkInterface(QWidget):
    """
     [ ][ ][ ] | [ ][ ][ ] | [ ][ ][ ]
     [ ][ ][ ] | [ ][ ][ ] | [ ][ ][ ]
     [ ][ ][ ] | [ ][ ][ ] | [ ][ ][ ]
     ---------------------------------
     [ ][ ][ ] | [ ][ ][ ] | [ ][ ][ ]
     [ ][ ][ ] | [ ][ ][ ] | [ ][ ][ ]
     [ ][ ][ ] | [ ][ ][ ] | [ ][ ][ ]
     ---------------------------------
     [ ][ ][ ] | [ ][ ][ ] | [ ][ ][ ]
     [ ][ ][ ] | [ ][ ][ ] | [ ][ ][ ]
     [ ][ ][ ] | [ ][ ][ ] | [ ][ ][ ]
 
     上記の画面を実現させるためのクラス．
    """
    def __init__(self, window_size, dimention, AnswerArray = None):
        super().__init__()
        # 数独は正方形なのでwidth = height
        self.whsize = window_size
        self.dim = dimention
        self.root_dim = int(math.sqrt(self.dim))
        # 答えの行列
        self.ans_array = AnswerArray
        # 罫線の太さ
        self.PEN_WEIGHT = 3

        self.initUI()
    
    def initUI(self):
        self.setFixedSize(self.whsize, self.whsize)
        self.layout = QGridLayout()
        self.nums_form = [[QLabel() for i in range(self.dim)] for j in range(self.dim)]
        font = QFont()
        FONT_SIZE = 26
        font.setPointSize(FONT_SIZE)
        for i in range(self.dim):
            for j in range(self.dim):
                numform = self.nums_form[i][j]
                # 解の書き込み
                numform.setText(f"{self.ans_array[i][j]}")
                # 枠線の太さ
                numform.setLineWidth(1)
                # 枠線のスタイル
                numform.setFrameStyle(QFrame.Box | QFrame.Plain)
                # 中央の数字を枠内の中央に配置
                numform.setAlignment(Qt.AlignCenter)
                numform.setFont(font)
                self.layout.addWidget(numform, i, j)
        
        # 枠同士の水平方向・垂直方向の間隔
        self.layout.setHorizontalSpacing(1)
        self.layout.setVerticalSpacing(1)
        # GridLayout全体を一つと見たとき，そのウィジェットの左右上下方向のmarginを0に
        self.layout.setContentsMargins(1,1,1,1)

        self.setLayout(self.layout)
    
    # 罫線を引く
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        split = self.root_dim
        #ウィジェットサイズを取得しているがself.whsizeがあるので不要な気がする
        rect = self.rect()
        step = rect.width() / split
        for i in range(0,split+1):
            painter.setPen(QPen(Qt.black, self.PEN_WEIGHT, Qt.SolidLine))
            x = step * i
            painter.drawLine(x,0,x,rect.height())
            painter.drawLine(0,x,rect.width(),x)

class SdkEditIF(SdkInterface):
    def initUI(self):
        self.setFixedSize(self.whsize, self.whsize)
        self.layout = QGridLayout()
        # 継承元のクラスから，変更した部分はQTextEditで，入力を受け付けられるようにする
        self.nums_form = [[QTextEdit() for i in range(self.dim)] for j in range(self.dim)]
        font = QFont()
        FONT_SIZE = 26
        font.setPointSize(FONT_SIZE)
        for i in range(self.dim):
            for j in range(self.dim):
                numform = self.nums_form[i][j]
                numform.setLineWidth(1)
                numform.setFrameStyle(QFrame.Box | QFrame.Plain)
                numform.setFont(font)
                numform.setAlignment(Qt.AlignCenter)
                
                self.layout.addWidget(numform, i, j)
        
        self.layout.setHorizontalSpacing(1)
        self.layout.setVerticalSpacing(1)
        self.layout.setContentsMargins(1,1,1,1)

        self.setLayout(self.layout)
    
    # 入力された数字をすべて消す
    def clearNums(self):
        for i in range(self.dim):
            for j in range(self.dim):
                self.nums_form[i][j].clear()
                self.nums_form[i][j].setAlignment(Qt.AlignCenter)
    
    # 今現在の行列の状態を返す関数
    def returnNumsArray(self):
        return self.nums_form