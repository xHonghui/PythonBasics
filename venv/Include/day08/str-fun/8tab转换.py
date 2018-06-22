mystr="1\t2\t3"  #\t转化为空格 默认8个，tabsize=1 指定空格数量
print(mystr.expandtabs(tabsize=1))
print(mystr.expandtabs(tabsize=10))

