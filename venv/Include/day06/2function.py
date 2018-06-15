# 四种函数定义方式
import random


# 无参数无返回值
def test1():
    print("hello world")


# 无参数有返回值
def test2():
    return random.randint(0, 10)


# 有输入无返回值
def test3(num):
    print("num=" + str(num))


# 有输入有返回值
def test4(a, b):
    return a + b


# 函数调用
test1()
num = test2()
print("num=" + str(num))
test3(12)
num = test4(1, 3)
print("num=" + str(num))
