# for 嵌套的实际使用例子
import turtle

# for i in range(0, 300, 100):
#     for j in range(0, 400, 100):
#         turtle.goto(j, i)
#         turtle.pendown()  # 跳过第一次
#         turtle.write(str(i) + "," + str(j))
#     turtle.penup()
#
# turtle.done()

# for i in range(0, 300, 100):
#     for j in range(0, 400, 100):
#         turtle.goto(j, i)
#         turtle.pendown()
#         turtle.write(str(i) + "," + str(j))
#     turtle.penup()
# turtle.done()

# for i in range(0, 300, 100):
#     for j in range(0, 400, 100):
#         turtle.goto(j, i)
#         turtle.pendown()
#         turtle.write(str(j) + "," + str(i))
#     turtle.penup()
# turtle.done()

# for 循环的进一步解析
# step > 0 ,则 a<b 才能执行循环， step < 0，则 a > b 才能执行
for i in range(0, 100, -10):  # 一次也不会执行
    print(str(i))

for i in range(100, 0, -10):  # 循环 10 次 依次为 100,90,80,70,60,50,40,30,20,10,  rang() ：区间为左闭右开
    print(str(i))
