# 匿名函数

# 匿名函数 1
fun_test = lambda mystr: print(mystr)
fun_test("hello python")

# 匿名函数 2
(lambda mystr: print(mystr))("hello python")  # 匿名调用

# 匿名函数3（多参数），匿名函数的函数体好像只能一行，不能多行
num = lambda a, b, c: print(a + b + c)
num(1, 2, 3)






















