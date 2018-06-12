import random

startNum = random.randint(1, 1000)
num = eval(input("请输入一个数字"))
while num != startNum:
    if num > startNum:
        print("big")
    else:
        print("small")
    num = eval(input("继续输入一个数"))
else:
    print("输入数字正确")

print("游戏结束")
