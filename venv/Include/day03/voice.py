import win32com.client  # 系统客户端包

speaker = win32com.client.Dispatch("SAPI.SPVOICE")
speaker.Speak("你是傻逼，你是傻逼")
speaker.Speak("you are similar B. you are similar B!")

speaker.Speak