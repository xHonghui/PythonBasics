# 且运算符
physicScore = 100
mathScore = 99
languageScore = 98

if physicScore >= 100 and mathScore >= 100 and languageScore >= 100:
    print("录取清华")
else:
    print("清华不行就北大咯")

# 或运算符
physicScore = 100
mathScore = 100
languageScore = 100

if physicScore >= 100 or mathScore >= 100 or languageScore >= 100:
    print("录取北大")
else:
    print("回家耕田吧")

# 逻辑运算符  取反
num1 = 99
boo = num1 >= 100
if not boo:
    print("考试不及格")

# 短路效应，和java 一样。不过python 中逻辑运算符返回值的并不一定是 True 或者 False
# 具体如下示例
num1 = 100
num2 = 99
num3 = 98

b = (num1 < num2 and num2 > num3)
print(b)  # False
b = (1 and 9 and 0 and 10)
print(b)  # 输出 0 ， 并不是 False，一有
b = (1 and 9 and -1 and 10)
print(b)  # 输出 10 ，并不是 True ，没有假 ，则一直检查到最后一个数并将最后一个数返回
b = (0 or 0 or 1 or 10)
print(b)  # 1 ，一遇到真，则直接返回
b = (0 or 0 or 0 or 0)
print(b)  # 全部为假，则返回最后一个，虽然最后一个也是假


# 逻辑运算符优先级

