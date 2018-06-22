mystr = "孙播	陈慧	申凌瑞	 陈慧  李佳奇	吴东	牛兴杰	"
print(mystr.index("陈慧"))  # index查找字符串是否存在，存在返回第一个下标，不存在，异常错误
print(mystr.rindex("陈慧"))  # rindex查找，返回最后一个的下表
print(mystr.index("陈慧", 7, 10))  # 第二个开始，第三个结束，查找结果不存在，异常错误

# 总结：index() rindex() 与 find() rfind() 函数的相同点与不同点：
# 相同点：都是查找一个字符串中是否包含另一个字符串，如果包含，则返回字符串的下标
# 不同点：查找不到时，find() rfind() 返回 -1  , index() rindex() 直接报异常错误