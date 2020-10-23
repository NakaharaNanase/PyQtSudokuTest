# PyQtSudokuTest
整数計画問題を解くパッケージPulpを使って素早くナンプレ(数独)を解こう！(現在はfeatureブランチにあります．conda環境でのPython3.7.6で動作確認をしており，これらのコードを動かすためには数理最適化ソルバーであるpulpパッケージが必要です．pulpをインストールするには，conda環境の場合，conda install -c [ご自身の環境にあったチャンネル名] pulpとターミナルで叩いてください．)

<br>
<br>
<br>

## SudokuAppのインターフェイスとinterfaceフォルダ
　見た目はこんな感じです．数字を入力すると，答えが新しいウィンドウで出現します．
これらの「見た目」に関する部分は，全てinterfaceフォルダにまとめています．PyQt5を利用して書いています．
<br>
![SudokuApp](https://user-images.githubusercontent.com/58910397/96371934-59dc1580-119f-11eb-957e-556d80238d40.png)

![SudokuApp_ans](https://user-images.githubusercontent.com/58910397/96959249-86df4e00-153a-11eb-8880-732ce3b5a24e.png)
<br>
<br>
画像の例題は[こちら](https://numpre7.com/np601004)から解くことができます．このアプリが求解までに要した時間は0.07秒ほどでした．

<br>
<br>
<br>

## engineフォルダ
　ナンプレは，数字を仮置きしていって「条件を満たすかどうか？」で判定していくアルゴリズムを用いて解く方法もありますが，
整数計画問題として定式化して求解する方法もあります．このアプリでは後者を採用しています．(そもそも整数計画問題として解きたいというところからこのアプリ開発を始めたので...)
generate_problem.pyは，calculation.pyで問題を解くための下準備をするもので，calculation.pyはpulpを用いて実際に与えられた問題を解くものです．

<br>
<br>
<br>

## calculation.pyの(1)-(5)の制約式について
<img src="https://latex.codecogs.com/gif.latex?x_{ijk}"/>を<img src="https://latex.codecogs.com/gif.latex?(i,&space;j)" />のマスに
数字<img src="https://latex.codecogs.com/gif.latex?k" />をいれるとき1，それ以外を0とする0-1変数とします．その時，数独の答えは，以下の条件を満たす必要があります．
<br>
<br>
<br>
### (1)任意の<img src="https://latex.codecogs.com/gif.latex?(i,&space;j)" />マスについて，1から9(9x9の場合)のうち何らかの数字<img src="https://latex.codecogs.com/gif.latex?k" />が1つ定まる
　<img src="https://latex.codecogs.com/gif.latex?\sum_{k=1}^9&space;x_{ijk}&space;=&space;1&space;\&space;\&space;(\forall&space;(i,&space;j)&space;)"/>

<br>
<br>

### (2)各<img src="https://latex.codecogs.com/gif.latex?i" />行の数字<img src="https://latex.codecogs.com/gif.latex?k" />について，その数字<img src="https://latex.codecogs.com/gif.latex?k" />が入る列は1つだけ
　<img src="https://latex.codecogs.com/gif.latex?\sum_{j=1}^9&space;x_{ijk}&space;=&space;1&space;\&space;\&space;(\forall&space;i,&space;\&space;\forall&space;k&space;)"/>

<br>
<br>

### (3)各<img src="https://latex.codecogs.com/gif.latex?j" />列の数字<img src="https://latex.codecogs.com/gif.latex?k" />について，その数字<img src="https://latex.codecogs.com/gif.latex?k" />が入る列は1つだけ
　<img src="https://latex.codecogs.com/gif.latex?\sum_{i=1}^9&space;x_{ijk}&space;=&space;1&space;\&space;\&space;(\forall&space;j,&space;\&space;\forall&space;k&space;)"/>

<br>
<br>

### (4)3x3の部分に，1から9の数字が入る
　<img src="https://latex.codecogs.com/gif.latex?\sum_{i=1}^9&space;\sum_{j=1}^9&space;x_{i&plus;u,&space;j&plus;v,k}&space;=&space;1&space;\&space;\&space;(\forall&space;k,&space;\&space;u,&space;v=\{0,&space;3,&space;6&space;\})"/>

<br>
<br>

### (5)<img src="https://latex.codecogs.com/gif.latex?(i,&space;j)" />のマスは数字<img src="https://latex.codecogs.com/gif.latex?m" />であるというヒント
　<img src="https://latex.codecogs.com/gif.latex?x_{ijm}&space;=&space;1&space;\&space;(\forall&space;(i,&space;\&space;j))"/>

<br>
<br>

pulpでは等式制約を扱えないので，<img src="https://latex.codecogs.com/gif.latex?\geq"/>や<img src="https://latex.codecogs.com/gif.latex?\leq"/>を用いて表現しています．
また，このプログラムでは，それらの制約を拡張させて16x16ナンプレや25x25ナンプレなどにも対応しています．

<br>

![SudokuApp25x25](https://user-images.githubusercontent.com/58910397/96374038-4a62c980-11ab-11eb-8987-92e4d0a9f376.png)

<br>
<br>
<br>

## main.py
　これを実行するとプログラムが始まります．
