from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from interface import main_window as mw
from . import buttons_widget as bw
from . import sudoku_interface as si

class CentralWidget(QWidget):
    """
     数独のインターフェイス画面と，ボタンウィジェットを垂直に積んで，
     中央ウィジェットを定義する．
    """
    def __init__(self, width, height, dimention):
        super().__init__()
        self.width = width
        self.height = height
        self.min_wh = min(self.width, self.height)
        self.dimention = dimention

        # 中央ウィジェットの中身のウィジェットを定義する
        self.sdk_interface_widget = si.SdkEditIF(self.min_wh, self.dimention)
        self.buttons_widget = bw.ButtonsWidget(self.width, self.height, self.min_wh, self.dimention, self.sdk_interface_widget)
        
        self.initUI()
    
    def initUI(self):
        # ウィンドウサイズについて横幅が高さに比べて大きいときは，
        # ボタン3つのウィジェットは数独画面の横に配置する
        if (self.width > self.height):
            self.layout = QHBoxLayout()
        else:
            self.layout = QVBoxLayout()
        
        self.layout.addWidget(self.sdk_interface_widget)
        self.layout.addWidget(self.buttons_widget)
        self.layout.setContentsMargins(0,0,0,0)

        self.setLayout(self.layout)
