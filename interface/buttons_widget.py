from PyQt5.QtWidgets import (QWidget, QPushButton, 
                             QHBoxLayout, QVBoxLayout)

from interface import main_window as mw
from . import sudoku_interface as si
from engine import generate_problem as gp
from engine import calculation as calc

class ButtonsWidget(QWidget):
    def __init__(self, width, height, min_wh, dimention, sdk_object):
        super().__init__()
        self.width = width
        self.height = height
        self.min_wh = min_wh
        self.dimention = dimention
        self.sdk = sdk_object
        
        # 3つのボタン(Solve, Reset, Quit)を設置
        self.solve_button = QPushButton("Solve")
        self.solve_button.clicked.connect(self.getAnswerWindow)
        
        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.sdk.clearNums)
        
        self.quit_button = QPushButton("Quit")
        self.quit_button.clicked.connect(mw.SudokuApp.quit)
        
        self.initUI()
    
    def initUI(self):
        # もし横幅のほうが大きければ，ボタン全体のウィジェットは水平配置になるので，
        # ボタン同士の配置を垂直配置にする．
        if (self.width > self.height):
            self.layout = QVBoxLayout()
        else:
            self.layout = QHBoxLayout()
        self.layout.addWidget(self.solve_button)
        self.layout.addWidget(self.reset_button)
        self.layout.addWidget(self.quit_button)
        self.setLayout(self.layout)
    
    # solveボタンを押したとき，求解して新しいウィンドウで答えを表示する
    # 数字以外のものを受け取ったときのエラー表示が必要．
    def getAnswerWindow(self):
        ProblemArray = gp.generateProblemArray(self.sdk.returnNumsArray(), self.dimention)
        problem = calc.CalcOptimalAns(ProblemArray)
        AnswerArray = problem.AnswerInfo()
        self.window = si.SdkInterface(self.min_wh, self.dimention, AnswerArray)
        self.window.show()
