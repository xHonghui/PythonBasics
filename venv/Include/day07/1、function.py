# 函数的两种类型（系统提供、自定义）
# import os
#
# print(type(os.system))  # <class 'builtin_function_or_method'> 系统函数
# print(id(os.system))  # 549143152608
#
#
# def add(num1, num2):
#     return num1 + num2
#
#
# print(type(add))  # <class 'function'> 自定义函数
# print(id(add))  # 549143125528


# 函数变量
# def add(num1, num2):
#     return num1 + num2
#
#
# def mul(num1, num2):
#     return num1 * num2
#
#
# print(add(1, 3))
#
# add = mul  # 函数变量赋值后，add 存储的是 mul 函数的地址，故执行乘法运算
# print(add(2, 3))

# 又或者
import os

print("tasklist")  # 输出函数
print = os.system
print("tasklist")  # 相当于 os.system("tasklist")

op = print
op("hello world")  # 相当于 print("hello world")
op = os.system
op("notepad")   # 相当于 os.system("notepad") 函数
