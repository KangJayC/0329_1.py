import math
import tkinter
from tkinter import *

root = Tk()
root.title('helloWorld')
# 窗口尺寸
# root.geometry('500x500')
# 固定尺寸
root.resizable(0, 0)

# 棋盘中一格边长
boxSize = 60
# 横向格子数
boxWidh = 8
# 纵向格子数
boxHigh = 9
wid = boxSize * boxWidh  # (60*8)
high = boxSize * boxHigh  # (60*9)
root_start_x = 20
root_start_y = 20
# 棋子半径
pointSize = 10
# 落子点
rootPoint = []
# 棋子位置
points = []
# 棋子本身
ovals = []
# 棋子颜色
colorFlag = True
# 5子相连为胜
winNum = 5
gameRunning = True

# 创建一个Canvas,上下各空root_start_x距离，左右各空root_start_y,中间放棋盘
cv = Canvas(root, width=wid + 2 * root_start_x, height=high + 2 * root_start_y, bg="lightblue", confine=True,
            cursor="circle")

rootBox = cv.create_rectangle(root_start_x, root_start_y, root_start_x + wid, root_start_y + high)

# 纵
for i in range(1, boxWidh):
    cv.create_line(root_start_x + i * (wid / boxWidh), root_start_y, root_start_x + i * (wid / boxWidh),
                   root_start_y + high, fill='red')

# 抹去河道线
line1 = root_start_y + (math.floor(boxHigh / 2)) * (high / boxHigh)
line2 = root_start_y + (math.ceil(boxHigh / 2)) * (high / boxHigh)
for i in range(1, boxWidh):
    cv.create_line(root_start_x + i * (wid / boxWidh), line1, root_start_x + i * (wid / boxWidh), line2,
                   fill='lightblue')
# 横
for i in range(1, boxHigh):
    cv.create_line(root_start_x, root_start_y + i * (high / boxHigh), root_start_x + wid,
                   root_start_y + i * (high / boxHigh), fill='red')

for i in range(0, boxHigh):
    for j in range(0, boxWidh + 2):
        rootPoint.append([root_start_x + i * (wid / boxWidh), root_start_y + j * (high / boxHigh)])
        # x1, y1 = (root_start_x+i * (wid / boxWidh) - 10), (root_start_y + j * (high / boxHigh) - 10)
        # x2, y2 = (root_start_x+i * (wid / boxWidh) + 10), (root_start_y + j * (high / boxHigh) + 10)
        # cv.create_oval(x1, y1, x2, y2, fill='black')


# 落子
def _paint(event):
    if not gameRunning:
        return
    global colorFlag
    # event.x 鼠标左键的横坐标
    # event.y 鼠标左键的纵坐标
    fix = fixPoint(event.x, event.y)
    if fix[0] == 0 and fix[1] == 0:
        outputLog("点在空白处")
        return
    for p in points:
        if p[0] == fix[0] and p[1] == fix[1]:
            outputLog("该点已存在落子")
            return
    outputLog("新增一颗子" + str(fix[0]) + "," + str(fix[1]) + ',' + str(colorFlag) + ",共" + str(len(points) + 1) + '颗棋子')
    x1, y1 = (fix[0] - pointSize), (fix[1] - pointSize)
    x2, y2 = (fix[0] + pointSize), (fix[1] + pointSize)
    oval = cv.create_oval(x1, y1, x2, y2, fill=getPointColor())
    ovals.append(oval)
    points.append([fix[0], fix[1], colorFlag])
    checkWin(fix[0], fix[1], colorFlag)
    colorFlag = bool(1 - colorFlag)


def outputLog(text):
    txt.configure(state='normal')
    txt.insert(END, text + '\n')
    txt.configure(state='disabled')


def getPointColor():
    if colorFlag:
        color = 'white'
    else:
        color = 'black'
    return color


# 校正鼠标位置
def fixPoint(x, y):
    diff = 10000
    fix_x = 0
    fix_y = 0
    for point in rootPoint:
        pX = point[0]
        pY = point[1]
        # outputLog(str(pX)+','+str(pY))
        # tmpDiff = math.fabs(pX-x) + math.fabs(pY-y)
        # if tmpDiff<diff:
        #     diff = tmpDiff
        #     fix_x = pX
        #     fix_y = pY
        if math.fabs(pX - x) < pointSize * 2 and math.fabs(pY - y) < pointSize * 2:
            fix_x = pX
            fix_y = pY
            break
    return [fix_x, fix_y]


# label.bind('<Button-1>', left_mouse_down)  # 鼠标左键按下
# label.bind('<ButtonRelease-1>', left_mouse_up)  # 鼠标左键释放
# label.bind('<Button-3>', right_mouse_down)  # 鼠标右键按下
# label.bind('<ButtonRelease-3>', right_mouse_up)  # 鼠标右键释放
# label.bind('<B1-Motion>', moving_mouse)  # 鼠标左键按下并移动
# label.bind('<Enter>', moving_into)  # 鼠标移入事件
# label.bind('<Leave>', moving_out)  # 鼠标移出事件
# label.bind('<FocusIn>', focus)  # 聚焦事件
# label.bind('<FocusOut>', unfocus)  # 失焦事件
# label.focus_set()  # 直接聚焦

# ,height=high,width=50
txt = Text(root, width=25, height=44)
txt.grid(row=0, column=1)

scroll = tkinter.Scrollbar()
scroll.grid(row=0, column=2, sticky='ns')
# scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)

# txt.configure(xscrollcommand=scroll.set)
scroll.config(command=txt.yview)


# 检查输赢算法
# 从落子点往左、往右，往上，往下、斜向左上、斜向右下、斜向左下、斜向右上
def checkWin(x, y, flag):
    xcnt1 = checkX_left(x, y, flag) + checkX_right(x, y, flag) + 1
    xcnt2 = checkY_top(x, y, flag) + checkY_down(x, y, flag) + 1
    xcnt3 = checkS_leftUP(x, y, flag) + checkS_rightDown(x, y, flag) + 1
    xcnt4 = checkS_leftDown(x, y, flag) + checkS_rightUP(x, y, flag) + 1
    outputLog(
        "xcnt1=" + str(xcnt1) + "," + "xcnt2=" + str(xcnt2) + "," + "xcnt3=" + str(xcnt3) + "," + "xcnt4=" + str(xcnt4))
    if xcnt1 >= winNum or xcnt2 >= winNum or xcnt3 >= winNum or xcnt4 >= winNum:
        global gameRunning
        gameRunning = False
        outputLog(getPointColor() + " Win!")


# 横向检查right
def checkX_right(x, y, flag, sameNum=1):
    cnt = 0
    for point in points:
        if point[2] == flag and point[1] == y and point[0] - x == boxSize * sameNum:
            cnt = 1 + checkX_right(x, y, flag, sameNum + 1)
    return cnt;


# 横向检查left
def checkX_left(x, y, flag, sameNum=1):
    cnt = 0
    for point in points:
        if point[2] == flag and point[1] == y and x - point[0] == boxSize * sameNum:
            cnt = 1 + checkX_left(x, y, flag, sameNum + 1)
    return cnt;


# 纵向检查top
def checkY_top(x, y, flag, sameNum=1):
    cnt = 0
    for point in points:
        if point[2] == flag and point[0] == x and point[1] - y == boxSize * sameNum:
            cnt = 1 + checkY_top(x, y, flag, sameNum + 1)
    return cnt;


# 纵向检查down
def checkY_down(x, y, flag, sameNum=1):
    cnt = 0
    for point in points:
        if point[2] == flag and point[0] == x and y - point[1] == boxSize * sameNum:
            cnt = 1 + checkY_down(x, y, flag, sameNum + 1)
    return cnt;


# 斜向检查左上
def checkS_leftUP(x, y, flag, sameNum=1):
    cnt = 0
    for point in points:
        if point[2] == flag and x - point[0] == boxSize * sameNum and y - point[1] == boxSize * sameNum:
            cnt = 1 + checkS_leftUP(x, y, flag, sameNum + 1)
    return cnt;


# 斜向检查右下
def checkS_rightDown(x, y, flag, sameNum=1):
    cnt = 0
    for point in points:
        if point[2] == flag and point[0] - x == boxSize * sameNum and point[1] - y == boxSize * sameNum:
            cnt = 1 + checkS_rightDown(x, y, flag, sameNum + 1)
    return cnt;


# 斜向检查左下
def checkS_leftDown(x, y, flag, sameNum=1):
    cnt = 0
    for point in points:
        if point[2] == flag and x - point[0] == boxSize * sameNum and point[1] - y == boxSize * sameNum:
            cnt = 1 + checkS_leftDown(x, y, flag, sameNum + 1)
    return cnt;


# 斜向检查右上
def checkS_rightUP(x, y, flag, sameNum=1):
    cnt = 0
    for point in points:
        if point[2] == flag and point[0] - x == boxSize * sameNum and y - point[1] == boxSize * sameNum:
            cnt = 1 + checkS_rightUP(x, y, flag, sameNum + 1)
    return cnt;


def clean():
    global points
    global gameRunning
    for oval in ovals:
        cv.delete(oval)
    points = []
    gameRunning = True
    txt.configure(state='normal')
    txt.delete('1.0', 'end')
    outputLog("重新开始一局")


menubar = Menu(root)
fmenu = Menu(menubar)
fmenu.add_command(label="go", command=clean)
menubar.add_cascade(label='Restart', menu=fmenu)

cv.grid(row=0, column=0)
cv.bind("<Button-1>", _paint)
root['menu'] = menubar

root.mainloop()

# 1.校正鼠标位置
# 2.判断落点是否已经有子
# 3.定义判输算法
# 4.人机算法