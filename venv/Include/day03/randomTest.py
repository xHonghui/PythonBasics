# random 随机数的生成
import random

num1 = random.randint(0, 10)  # 闭区间
num2 = random.randint(0, 10)
print("num1=" + str(num1))
print("num2=" + str(num2))

num1 = random.randrange(0, 10)  # 左闭右开
num2 = random.randrange(0, 10)
print("num1=" + str(num1))
print("num2=" + str(num2))








