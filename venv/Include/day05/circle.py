# 控制一个窗体沿着圆的路径转动
import win32con
import win32gui
import math

# 角度与数值之间的转换
# π=180°，1=（180/π）°
# 1≈ 57.2957796
# 定义SE作为角度，初始值为 0.0，逐步＋0.1，直到 3.1415926535
# math 中的三角函数，将数值传入，会默认将其转换为对应的角度再求职，因为在电脑中好像不能直接输入角度数据
notepad = win32gui.FindWindow("Notepad", "无标题 - 记事本")
while True:
    SE = 0.0  # 角度
    while (SE - 3.1415926535 * 2) < 0.000001:
        # 圆心：（600,300）
        # 根据半径、角度、圆心位置求圆的周边点的坐标
        newx = int(600 + 300 * math.cos(SE))
        newy = int(300 + 300 * math.sin(SE))
        win32gui.SetWindowPos(notepad,
                              win32con.HWND_TOPMOST,
                              newx,
                              newy,
                              200,
                              200,
                              win32con.SWP_SHOWWINDOW)
        SE += 0.01
