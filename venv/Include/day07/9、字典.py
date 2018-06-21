# 字典，key - value 的组合，相当于 java 中的 map

mydict = {"abcdefg": 10, "123456": 2, "xyzhjk": 3, "123456": 10}
print(type(mydict))  # dict是set的强化版 左边是key,不允许重复，右边value，可重复
print(mydict)
print(mydict["abcdefg"])  # 根据key取出value
print(mydict.values())  # 值，输出全部的值（不输出键）
for key in mydict:  # 循环字典
    print(key, mydict[key])
