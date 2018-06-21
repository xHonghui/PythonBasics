# 数据转换类型
print(int("123"))  # 转换为 int 类型
print(int(123.321))  # 取整
print(float("123.321"))  # 转换为 float 类型
print(ord("1"))  # 将字符转换为编码集合 的编号
print(chr(49))  # 将字符编号转换为字符
print(str(99) + str(100))  # 将 X 转换为字符串
print(eval("456"))  # 转换为数值

print(list((1, 2, 3, 4, 5)))  # 转换为 list[]
print(tuple([1, 2, 3, 4, 5]))  # 转换为 元组（tuple）
print(set((1, 2, 3, 4, 5)))  # 转换为 set
print(dict({"1": 1, "2": 2}))  # 字典

print(repr(1 + 2 + 3))  # 将对象转换为表达式字符串
print(repr("1+2+3"))

# 进制转换
print(int("10",16))  # 将对象 x 转换为整数并指定进制
print(hex(10))   # 将整数转换为 16 进制
print(oct(10))  # 将整数转换为 8 进制