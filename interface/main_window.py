from PyQt5.QtWidgets import QApplication, QMainWindow
from . import central_widget as cw

class SudokuApp(QApplication):
    """
     Qtにおいて，メインウィンドウを表示させる前に必ず生成する必要がある
     ウィジェットであるQApplicationをここで定義する．
     DIMENTIONは，解く数独の次元(サイズ)，デフォルトは9x9数独なので，
     DIMENTION=9としてあるが，今後16x16や25x25に拡張できるようにしてある．
    """
    def __init__(self, argv, width, height, DIMENTION = 9):
        super().__init__(argv)
        self.dimention = DIMENTION
        self.window = MainWindow(width, height, self.dimention)
        #ウィンドウを表示する
        self.window.show()

class MainWindow(QMainWindow):
    """
     このSudokuアプリを起動した時に真っ先に現れる画面のクラス．
     数独のインターフェイスとボタンのウィジェットを垂直に積んだ,
     QVBoxLayoutをCentralWidget(中央ウィジェット)として配置している．
    """
    def __init__(self, width, height, dimention):
        super().__init__()
        self.width = width
        self.height = height
        self.dim = dimention
        self.title = "SudokuApp"
        self.c_wid = cw.CentralWidget(self.width, self.height, self.dim)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        self.setCentralWidget(self.c_wid)