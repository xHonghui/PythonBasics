print("逗逼is you".startswith("1逗"))  # 判断是否开头

# 函数 swapcase() 字符串大小写切换
# 如果是大写，则切换为小写，如果是小写，则切换为大写
mystr = "hello world"
mystr1 = "HELLO world"
print(mystr.swapcase())  # HELLO WORLD
mystr = mystr.swapcase()
print(mystr.swapcase())  # 切换，不会改变原来的

print(mystr1.swapcase())
mystr1 = mystr1.swapcase()
print(mystr1.swapcase())

# 金融数据，长度为 10 ,不足在前面补 0
print("123".zfill(10))  # 金融数据
