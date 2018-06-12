# while else 的使用
# num1 = 0
# while 0:
#     print("")
# else:
#     print("")

# while 处理 Float 类型数据
# num = 2.0
# while num > 0:
#     num -= 0.1
#     print(str(num))
# else:
#     print("end")
# # 循环 20 次

password = input("请输入密码")
while password != "123456":
    password = input("密码错误，请重新输入")
else:
    print("密码正确，验证成功")

password = input("请输入密码")
while password != "123456":
    password = input("密码错误，请重新输入")
else:
    print("密码正确，验证成功")
