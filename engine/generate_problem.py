#数字が入力された行列を受け取って，calculation.pyが計算しやすい形にする関数
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