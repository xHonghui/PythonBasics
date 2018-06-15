# 成员变量
# member = 10  # 全局变量
#
#
# def test():
#     member = 5  # 局部变量
#     print(member, id(member))
#
#
# def test2():
#     global member  # 使用 global 引用全局变量
#     member = 10
#     print(member, id(member))
#
#
# test()
# test2()
# print(member, id(member))


# 函数嵌套以及 nonlocal 关键字的使用
def test3():
    num = 10

    def test4():
        nonlocal num  # 在函数嵌套使用中，内部函数使用 nonlocal 关键字来修改外部函数的变量
        num = 100
        print(num)

    test4()
    print(num)


test3()

# def test3():
#     num = 10
#
#     def test4():
#         num = 10
#         print(num, id(num))
#
#     test4()
#     print(num, id(num))
#
#
# number = 100
# number2 = 100
# print(id(number), id(number2))
#
# test3()
