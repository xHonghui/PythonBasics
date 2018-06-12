# 植物大战僵尸
import win32api
import win32gui
import win32process
import ctypes
import time

# 使用系统最高权限运行
PROCESS_SYSTEM_API = (0x000F0000 | 0x00100000 | 0xFFF)
# 通过窗体名称和标题获取 植物大战僵尸的窗体
window = win32gui.FindWindow("MainWindow", "植物大战僵尸中文版")
# 根据窗体获取进程ID
hid, pid = win32process.GetWindowThreadProcessId(window)
# 通过进程 ID 使用系统最高权限打开进程
phand = win32api.OpenProcess(PROCESS_SYSTEM_API, False, pid)
# 存储指定内存空间数值的变量
data = ctypes.c_long()
newdata = ctypes.c_long(500)
mydll = ctypes.windll.LoadLibrary("C:\\Windows\\System32\\kernel32.dll")
while True:
    # 加载系统内核
    # 获取指定内存空间的数据
    # int(phand)：打开的进程编号，c 语言中是 long 类型，python 中只有int 类型，所以int(phand)
    # 330330512 ：指定进程的指定内存地址，通过工具查找，工具使用 c 语言查找
    # ctypes.byref(data) : 或者的数据存于 data 中
    # 4 : 整数 4 字节
    # None : 所有
    mydll.ReadProcessMemory(int(phand), 330330512, ctypes.byref(data), 4, None)
    if data.value < 300:
        mydll.WriteProcessMemory(int(phand), 330330512, ctypes.byref(newdata), 4, None)
    time.sleep(1)
