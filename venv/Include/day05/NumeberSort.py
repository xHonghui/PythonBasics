# 数值排序
# num = eval(input("请输入数据的个数"))
# i = 0
# while i < num:
#     data = eval(input("请输入第" + str(i) + "个数："))
#     print(str(data))
#     i += 1

# 改造
# num = eval(input("请输入数据的个数"))
# maxdata = eval(input("请输入第1个数"))
# print(str(maxdata))
# i = 0
# while i < (num - 1):
#     data = eval(input("请输入第个数："))
#     if data > maxdata:
#         maxdata = data
#     print(str(data))
#     i += 1
# print("max:" + str(maxdata))

# 从一串数据中找出最大的和第二大的数
# num = eval(input("请输入数据的个数"))
# data = eval(input("请输入第一个数："))
# maxdata = data
# second = data
# i = 0
# while i < (num - 1):
#     data = eval(input("请输入第" + str(i + 1) + "个数"))
#     if data > maxdata:
#         second = maxdata
#         maxdata = data
#     print(str(data))
#     i += 1
# print("maxdata:" + str(maxdata), "seconddata:" + str(second))

# 数据交换
# 普通交换，第三方变量

a = 10
b = 20
a, b = b, a  # 交换数据
print(a, b)
