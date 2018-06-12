# 循环图形
import turtle

widthBase = 50
heightBase = 25
step = 10
num = 0
while num < 30:
    print("开始绘制")
    x1 = widthBase + step * num
    y1 = heightBase + step * num

    x2 = -widthBase - step * num
    y2 = heightBase + step * num

    x3 = - widthBase - step * num
    y3 = -heightBase - step * num

    x4 = widthBase + step * num
    y4 = -heightBase - step * num

    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x4, y4)
    turtle.goto(x1, y1)
    num+=1

else:
    print("绘制完成")

turtle.done()
