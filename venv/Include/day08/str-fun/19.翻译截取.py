mystr = "hello  python 我，我，你"
# 表
table = str.maketrans("op我你", "12他妹")  # o-1  p-2  我->
print(mystr.translate(table))  # 翻译替换
print(mystr.translate(table))
print(mystr.replace(" ", ""))  # 去除空格
