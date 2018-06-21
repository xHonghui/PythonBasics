# 字符串常识
numstr = "number"
print(len(numstr))
# for c in numstr:  # 遍历字符串
#     print("----" + c + "----")
# for i in range(len(numstr)):
#     print("---" + numstr[i] + "---")

# 字符串截取，相当于java 中的 substring()，区间是左闭右开
mystr = "notepad"
print(mystr[0:10])  # 字符串截取
print(mystr[1:-1])  # -1 负数从字符串的后面开始算起
print(mystr[:5])  # 从第一个字符开始
print(mystr[:])  # 全部字符
print(mystr[3:])  # 从索引3开始到最后一个（包括最后一位）
print(mystr * 3)  # 连续拷贝三次 mystr 字符串

# 字符串原理
mystr = "cmd"
print(id(mystr))
print(mystr[0])
# mystr[0]='A'  # 不可以修改字符串的某个字符
mystr="Amd"  # 可以这样修改
print(id(mystr))
print(mystr)
# 字符串可以调到新的字符串地址，但是不可以改变常量字符串
