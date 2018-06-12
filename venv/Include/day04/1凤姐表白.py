# 使用window 系统的语音功能进行语音合成，需要安装一个调用 window 系统API 的库，该库为 pywin32
# 在这个demo中，遇到了一个问题，安装了 pywin32 后，在pycharm 中执行程序一直报错找不到系统库，原因是
# 默认创建python 项目时，pycharm 会自动在项目的相应目录下生成一份python.exe（你的电脑需要安装有python.exe并配置好环境变量）
# 这样自动生成的python.exe没有包含（关联） pywin32 的库，自然也就报错找不到该库了。
import win32com.client  # 系统客户端包

speaker = win32com.client.Dispatch("SAPI.SPVOICE")  # 系统接口
# speaker.Speak("我是凤姐，我爱死了申凌睿")
# speaker.Speak("  i  am   luoyufeng, i  Love  shenlinrui  forever")

# while 循环
while True:
    speaker.Speak("你是傻逼你是傻逼")

while None:  # False
    print("为 true 则循环，为false 则不循环")



