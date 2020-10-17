import pulp
import math

class CalcOptimalAns(object):
    def __init__(self, ProblemInfo):
        #問題の情報として，初期値行列，次元が与えられる．9x9ナンプレならdim = 9, 16x16ナンプレならdim = 16
        self.__Array, self.__dim = ProblemInfo

        self.__x = {}
        self.__D = [i for i in range(1, self.__dim + 1)]
        #数独の答えを保存するもので，初期に与えられている数字はそのまま答えの一部になる．
        self.__Answer = self.__Array
        self.solveProblem()
    #数理最適化ソルバーを用いて与えられた問題を解く
    def solveProblem(self):
        problem = pulp.LpProblem("SudokuProblem")
        SudokuArray = {}
        #数独行列を生成．これが計算過程を経て答えになる．
        for i in self.__D:
            for j in self.__D:
                SudokuArray[i,j] = self.__Array[self.__D.index(i)][self.__D.index(j)]
        #変数宣言
        for i in self.__D:
            for j in self.__D:
                for k in self.__D:
                    self.__x[i,j,k] = pulp.LpVariable("x({:},{:},{:})".format(i,j,k), cat = "Binary")
        #制約関数
        #(1)
        for i in self.__D:
            for j in self.__D:
                problem += sum(self.__x[i,j,k] for k in self.__D) <= 1
                problem += sum(self.__x[i,j,k] for k in self.__D) >= 1
        #(2)
        for i in self.__D:
            for j in self.__D:
                problem += sum(self.__x[i,k,j] for k in self.__D) <= 1
                problem += sum(self.__x[i,k,j] for k in self.__D) >= 1
        #(3)
        for i in self.__D:
            for j in self.__D:
                problem += sum(self.__x[k,j,i] for k in self.__D) <= 1
                problem += sum(self.__x[k,j,i] for k in self.__D) >= 1
        #(4)
        #あとで拡張する必要あり．
        root_dim = int(math.sqrt(self.__dim))
        U = [i for i in range(0, self.__dim, root_dim)]
        for u in U:
            for v in U:
                for k in self.__D:
                    problem += sum(sum(self.__x[i+u, j+v, k] for j in range(1, root_dim+1)) for i in range(1, root_dim+1)) >= 1
                    problem += sum(sum(self.__x[i+u, j+v, k] for j in range(1, root_dim+1)) for i in range(1, root_dim+1)) <= 1
        #(5)
        for i in self.__D:
            for j in self.__D:
                if SudokuArray[i,j] != 0:
                    problem += self.__x[i,j,SudokuArray[i,j]] >= 1
                    problem += self.__x[i,j,SudokuArray[i,j]] <= 1

        problem.solve()
    #答えの数独行列を生成し，その行列を返す．
    def AnswerInfo(self):
        for i in self.__D:
            for j in self.__D:
                for k in self.__D:
                    if self.__x[i,j,k].value() == 1:
                        self.__Answer[self.__D.index(i)][self.__D.index(j)] = k
        return (self.__Answer, self.__dim)