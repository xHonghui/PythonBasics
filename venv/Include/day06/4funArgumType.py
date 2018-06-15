# 函数变量


def add(num1, num2):
    return num2 + num1


def sub(num1, num2):
    return num1 - num2


# 函数变量 go
# go = add
# print(go(3, 1))
# go = sub
# print(go(3, 1))


def test(go, num1, num2):
    return go(num1, num2)


# 函数变量的使用，可以直接作为参数进行函数变量的传递
print(test(add, 1, 2))
print(test(sub, 3, 4))


# None 函数
def test2():
    a = 10


print(test2())  # 输出 None，test2无返回值或者有返回值但是返回了 None


# 函数名称参数和位置参数
def test3(num1, num2, num3):
    print(num1, num2, num3)


test3(1, 2, 3)  # 位置参数
test3(num1=2, num2=3, num3=4)  # 名称参数


# 返回多个值的函数
def test4():
    return 1, 2


def test5():
    return 1, 2, 3


print("=====================================")
num = test4() # (1, 2) 使用一个变量来接收多个返回值的函数返回值
print(num)
num1, num2 = test4()  # 按前后顺序依次赋值给接收的变量
print(num1, num2)
num1, num2, num3 = test5()  # 按前后顺序依次赋值给接收的变量
print(num1, num2, num3)


