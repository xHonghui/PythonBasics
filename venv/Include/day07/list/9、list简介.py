# list 基本使用
import codecs

mylist = [1, 2, 3, 4, 5, 6, 7, 8]
mylist.append(9)
print(mylist)
print(len(mylist))

# 遍历
for ch in mylist:
    print(ch, end=" ")

print(mylist[2:6])  # 索引 2 到索引 6
print(mylist[2:])  # 索引 2 开始
print(mylist[:6])  # 首个开始到索引 6 位置
print(mylist[:])  # 全部输出
print(mylist * 2)  # mylist 复制两次

mylist2 = [19, 29, 39]
print(mylist + mylist2)  # 输出 [1, 2, 3, 4, 5, 6, 7, 8, 9, 19, 29, 39]

# 基本用途
file = codecs.open("E:\\python\\video\\千锋Python基础视频\\day7\\kaifangX.txt", "rb", "gbk", "ignore", 1)  # 读取文件
mylist = file.readlines()  # 一行一行读取，并将每行分开存于 mylist 集合中
while True:
    name = input("请输入需查询的名称")
    for line in mylist:
        if line.find(name) != -1:
            print(line)

