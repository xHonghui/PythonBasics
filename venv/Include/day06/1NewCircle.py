# 函数定义
import win32con
import win32gui
import math


# 函数的定义（python语法中，不同代码块之间的间隔也很严格，比如空一行或者空两行）
# 函数命名不能用大写
# 函数参数不能用大写
def draw_circle(winclassname, title):
    window = win32gui.FindWindow(winclassname, title)
    SE = 0.0
    while SE < 3.1415926535 * 2:
        newx = int(600 + 300 * math.cos(SE))
        newy = int(300 + 300 * math.sin(SE))
        win32gui.SetWindowPos(window,
                              win32con.HWND_TOPMOST,
                              newx,
                              newy,
                              200,
                              200,
                              win32con.SWP_SHOWWINDOW)
        SE += 0.1


# 函数的调用
while True:
    draw_circle("Notepad", "无标题 - 记事本")
    draw_circle("TXGuiFoundation", "QQ")
