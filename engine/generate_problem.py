def generateProblemArray(QTextEditArray, dimention):
        NumArray = [[0 for i in range(dimention)] for j in range(dimention)]
        #行列の生成
        for i in range(dimention):
            for j in range(dimention):
                num = QTextEditArray[i][j].toPlainText()
                if num == "":
                    pass #数字が入力されていない部分は0のままでよい
                else:
                    NumArray[i][j] = int(num)
        return (NumArray, dimention)

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication, QTextEdit
    app = QApplication(sys.argv)
    dim = 9
    Array = [[QTextEdit() for i in range(dim)] for j in range(dim)]
    
    B = generateProblemArray(Array, dim)
    print(B)
    sys.exit(app.exec_())