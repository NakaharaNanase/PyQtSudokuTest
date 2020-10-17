from PyQt5.QtWidgets import (QWidget, QPushButton, 
                             QHBoxLayout, QVBoxLayout)

class ButtonsWidget(QWidget):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        # 3つのボタン(Solve, Reset, Quit)を設置
        self.solve_button = QPushButton("Solve")
        self.reset_button = QPushButton("Reset")
        self.quit_button = QPushButton("Quit")
        self.initUI()
    
    def initUI(self):
        if (self.width > self.height):
            self.layout = QVBoxLayout()
        else:
            self.layout = QHBoxLayout()
        self.layout.addWidget(self.solve_button)
        self.layout.addWidget(self.reset_button)
        self.layout.addWidget(self.quit_button)
        self.setLayout(self.layout)