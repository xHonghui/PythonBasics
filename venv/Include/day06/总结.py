# day6 总结


# 字符串检索，
# print("hello".find("el")) # find函数找到返回位置
# print("hello".find("ak"))

import codecs  # 编码

# 第一个参数路径，第二个参数，rb二进制读写 第三个参数汉字编码，第十四个参数忽略错误
file = codecs.open("E:\\python\\video\\千锋Python基础视频\\day6\\kaifangX.txt", "rb", "gbk", "ignore")

while True:
    mystr = input("输入要查询的数据")
    while True:
        linestr = file.readline()  # 读取一行
        if linestr.find(mystr) != -1:
            print(linestr, end="")  # 显示数据
        if linestr == None:  # 读取失败返回值为None
            break


