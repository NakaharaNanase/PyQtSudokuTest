from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
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
        self.dimention = dimention
        self.sdk_window_size = min(self.width, self.height)
        self.sdk_interface_widget = si.SdkInterface(self.sdk_window_size, self.dimention)
        self.buttons_widget = bw.ButtonsWidget(self.width, self.height)
        self.initUI()
    
    def initUI(self):
        if (self.width > self.height):
            self.layout = QHBoxLayout()
        else:
            self.layout = QVBoxLayout()
        self.layout.addWidget(self.sdk_interface_widget)
        self.layout.addWidget(self.buttons_widget)
        self.layout.setContentsMargins(0,0,0,0)

        self.setLayout(self.layout)
