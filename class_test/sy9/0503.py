import sys
#sys模块是最常用的和python解释器交互的模块,
# sys模块可供访问由解释器(interpreter)使用或维护的变量和与解释器进行交互的函数。
# sys 模块提供了许多函数和变量来处理 Python 运行时环境的不同部分。
import tkinter#Tkinter 是 Python 自带的图形界面库，库中包含众多图形界面控件
from tkinter import *
from tkinter.messagebox import *
#这篇文章主要介绍了python中的tkinter库弹窗messagebox，包括消息提示框、消息警告框、错误消息框
import self as self


def startGame():
    global turn, board
    turn = True
    board = [[0 for i in range(15)] for j in range(15)] #创建一个15行15列的二维表，并初始化数组元素为0
    #初始化棋盘
    drawBoard()


def exit():
    win.destroy()#关闭窗口
    sys.exit()#退出程序，正常退出时exit(0)


def about():
    showinfo("About", "Gobang v0.1")


def drawBoard():
    global canvas, board
    canvas.delete("all")
    for i in range(15):
        canvas.create_line(30, 30 + 40 * i, 30 + 40 * 14, 30 + 40 * i, width=1, fill='black')
    for j in range(15):
        canvas.create_line(30 + 40 * j, 30,  30 + 40 * j, 30 + 40 * 14, width=1, fill='black')
        #前两个开始坐标，后两个结束坐标

    for i in range(15):
        for j in range(15):
            if board[i][j] == 0: #0是空白
                continue
            elif board[i][j] == -1:#-1是黑色
                color = 'black'
            else:
                color = 'white'#1是白色
            canvas.create_oval(40 * j + 15, 40 * i + 15, 40 * j + 45, 40 * i + 45, fill=color)

def onMouseUp(event):

    global turn
    x, y = event.x, event.y #捕获鼠标搜索事件
    if x > 10 and x < 610 and y > 10 and y < 610: #保证鼠标不在边缘处
        n = (x - 10) // 40 #Python3中是向下取整，a//b得到的值为a/b得到的最小整数
        m = (y - 10) // 40 #若在最边缘610 则该值为610/40=15.25  ==15  保证在框架内
        board[m][n] = -1 if turn else 1 #如果该区域是黑棋，则再下的就是白棋 覆盖
        drawBoard()
        if isWin(turn):
            showinfo("Gobang", "黑棋获胜!" if turn else "白棋获胜！")
            startGame()
        turn = not turn




def chessman_count(self,y, x, color_count):
        count1,count2, count3, count4 = 1, 1, 1, 1
        # 横计算
        for i in range(-1, -5, -1):
            if self.db[y][x + i] == color_count:

                count1 += 1
            else:
                break
        for i in range(1, 5, 1):
            if self.db[y][x + i] == color_count:
                count1 += 1
            else:
                break
        # 竖计算
        for i in range(-1, -5, -1):
            if self.db[y + i][x] == color_count:
                count2 += 1
            else:
                break
        for i in range(1, 5, 1):
            if self.db[y + i][x] == color_count:
                count2 += 1
            else:
                break
        # /计算
        for i in range(-1, -5, -1):
            if self.db[y + i][x + i] == color_count:
                count3 += 1
            else:
                break
        for i in range(1, 5, 1):
            if self.db[y + i][x + i] == color_count:
                count3 += 1
            else:
                break
        # \计算
        for i in range(-1, -5, -1):
            if self.db[y + i][x - i] == color_count:
                count4 += 1
            else:
                break
        for i in range(1, 5, 1):
            if self.db[y + i][x - i] == color_count:
                count4 += 1
            else:
                break

        return max(count1, count2, count3, count4)

def game_win(self, y, x, color_count):
        if self.chessman_count(y, x, color_count) >= 5:
            self.flag_win = 1
            self.flag_empty = 0
            return 1
        else:
            return 0


def isWin(turn):
    pass






























win = tkinter.Tk() # 创建一个 Tk 类实例 root = tkinter.Tk()
    # 我们习惯称这个 Tk 实例为 "root", "master" 或者 "app" 等等.       实例化一个窗体对象
win.wm_title("Gobang")#设置该窗体的标题为Gobang
win.resizable(False, False)#resizable()方法用于允许Tkinter根窗口根据用户需要更改其大小，我们也可以禁止调整Tkinter窗口的大小

menubar = Menu(win)#Menu(菜单)组件用于实现顶级菜单、下拉菜单和弹出菜单
win['menu'] = menubar
gamemenu = Menu(win)
helpmenu = Menu(win)
menubar.add_cascade(menu=gamemenu, label='Game') #Menu add_cascade 多级菜单
menubar.add_cascade(menu=helpmenu, label='Help')
gamemenu.add_command(label='start', command=startGame) #command命令
gamemenu.add_separator() #add_separator 分割线
gamemenu.add_command(label='Exit', command=exit)
helpmenu.add_command(label='About', command=about)

canvas = tkinter.Canvas(win, width=620, height=620, bg='lightyellow')
canvas.pack() #使用了pack()方法进行默认的Pack布局
canvas.bind("<ButtonRelease-1>", onMouseUp)#绑定鼠标事件并获取事件属性

board = []
turn = True
startGame()
win.mainloop()#进入等待与处理窗口事件
#1、mainloop()方法允许程序循环执行，并进入等待和处理事件。
# 窗口中的组件可以理解为一个连环画.
# 2、mainloop()方法的作用是监控每个组件，当组件发生变化或触发事件时，会立即更新窗口。
