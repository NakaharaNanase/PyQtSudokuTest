from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from interface import main_window as mw
from . import buttons_widget as bw
from . import sudoku_interface as si
from engine import generate_problem as gp
from engine import calculation as calc

class CentralWidget(QWidget):
    """
     数独のインターフェイス画面と，ボタンウィジェットを垂直に積んで，
     中央ウィジェットを定義する．
    """
    def __init__(self, width, height, dimention):
        super().__init__()
        self.width = width
        self.height = height
        self.sdk_window_size = min(self.width, self.height)
        self.dimention = dimention

        # 中央ウィジェットの中身のウィジェットを定義する
        self.sdk_interface_widget = si.SdkEditIF(self.sdk_window_size, self.dimention)
        self.buttons_widget = bw.ButtonsWidget(self.width, self.height)
        
        self.initUI()
        self.buttons_action()
    
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
    
    # ボタンを押した時の動作について定義する．
    def buttons_action(self):
        self.buttons_widget.solve_button.clicked.connect(self.getAnswerWindow)
        self.buttons_widget.reset_button.clicked.connect(self.reset_action)
        self.buttons_widget.quit_button.clicked.connect(mw.SudokuApp.quit)
    
    # solveボタンを押したとき，求解して新しいウィンドウで答えを表示する
    # 数字以外のものを受け取ったときのエラー表示が必要．
    def getAnswerWindow(self):
        ProblemArray = gp.generateProblemArray(self.sdk_interface_widget.returnNumsArray(), self.dimention)
        problem = calc.CalcOptimalAns(ProblemArray)
        AnswerArray = problem.AnswerInfo()
        self.window = si.SdkInterface(self.sdk_window_size, self.dimention, AnswerArray)
        self.window.show()
    
    # Resetボタンを押したときの動作，解を表示したウィンドウがあればそれも閉じる
    def reset_action(self):
        self.sdk_interface_widget.clearNums()
        #self.window.close()