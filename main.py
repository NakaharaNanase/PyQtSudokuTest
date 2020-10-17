import sys

from interface import main_window as mw

def main():
    #表示するメインウィンドウの幅と高さの設定
    WIDTH = 400
    HEIGHT = 500
    #数独アプリケーションのインスタンスを生成
    app = mw.SudokuApp(sys.argv, WIDTH, HEIGHT)
    #SudokuAppを閉じる操作をしない限り，終わりにしない
    sys.exit(app.exec_())

#実行
main()