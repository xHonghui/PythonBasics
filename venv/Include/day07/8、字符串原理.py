mystr = "cmd"
print(id(mystr))
print(mystr[0])
# mystr[0]='A'  # 不可以修改字符串的某个字符
mystr="Amd"  # 可以这样修改
print(id(mystr))
print(mystr)
# 字符串可以调到新的字符串地址，但是不可以改变常量字符串
