# 可变参数


def fun(*num):
    max_num = 0
    for i in num:
        max_num += i
    print(max_num)


fun(1, 2)
fun(1, 2, 3)
fun(1, 2, 3, 4)
fun(1, 2, 3, 4, 5)
