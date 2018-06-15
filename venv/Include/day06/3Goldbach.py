# 使用函数实现哥德巴赫猜想
# python 语法中一个函数的代码块与其他代码块前后都需要有两行空行，多了或者少了都会报警告


# 判断一个数是否为质数
def is_prime_number(num):
    if num == 0 or num == 1:
        return True
    elif num == 2 or num == 3:
        return True
    else:
        isprime = True
        for i in range(2, num):
            if num % i == 0:
                isprime = False
        return isprime


# 列举一个数的左右哥德巴赫猜想数列
def goldbach(num):
    for i in range(1, num):
        if is_prime_number(i) and is_prime_number(num - i):
            print(i, num - i)


for i in range(100, 200):
    print("===================" + str(i) + "start =======================")
    goldbach(i)  # 列举所有哥德巴赫猜想数列
    print("===================" + str(i) + "end =======================")

# 函数的本质就是内存地址，类型为 function
print(id(goldbach))  # 1078240730920
print(type(goldbach))  # <class 'function'>
