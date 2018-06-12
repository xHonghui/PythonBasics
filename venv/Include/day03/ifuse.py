# 条件表达式 if 的使用
temp = "you"
if temp == "you":  # 使用 ':'来分隔，java 中不需要
    print("yes yes yes !!!!")
print("hello word")

# if 和 else 后面都需要加上 “：”来和具体的业务代码进行分隔
if temp == "you":
    print("yes yes yes!!!")
else:
    print("nice nice nice")

# if 语句的自动 Bool 类型转换
# if 会将所有数据转换为 Bool 类型
# if("") 为 False，if("非空") 为 True
# if(0) 为 False， if(非0) 为 True
print(int(True))  # 1
print(int(False))  # 0

print(bool(1))  # True
print(bool(0))  # False
print(bool(-1))  # True
print(bool(2))  # True

print("str", bool(""))  # False
print("str", bool("非空字符"))  # True

if -1:  # True
    print("hello python")


