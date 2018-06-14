import win32gui
import win32con
import time
import math

wangwang = win32gui.FindWindow("Notepad", "无标题 - 记事本")
while True:
    for size in range(0, 800, 10):
        win32gui.SetWindowPos(wangwang,  # 操作记事本
                              win32con.HWND_TOPMOST,  # 最上方
                              size,  # 位置x
                              0,  # 位置y
                              300,  # 长度
                              300,  # 宽度
                              win32con.SWP_SHOWWINDOW)
    for size in range(0, 600, 10):
        win32gui.SetWindowPos(wangwang,  # 操作记事本
                              win32con.HWND_TOPMOST,  # 最上方
                              800,  # 位置x
                              size,  # 位置y
                              300,  # 长度
                              300,  # 宽度
                              win32con.SWP_SHOWWINDOW)
    for size in range(800, 0, -10):
        win32gui.SetWindowPos(wangwang,  # 操作记事本
                              win32con.HWND_TOPMOST,  # 最上方
                              size,  # 位置x
                              600,  # 位置y
                              300,  # 长度
                              300,  # 宽度
                              win32con.SWP_SHOWWINDOW)
    for size in range(600, 0, -10):
        win32gui.SetWindowPos(wangwang,  # 操作记事本
                              win32con.HWND_TOPMOST,  # 最上方
                              0,  # 位置x
                              size,  # 置y
                              300,  # 长度
                              300,  # 宽度
                              win32con.SWP_SHOWWINDOW)
