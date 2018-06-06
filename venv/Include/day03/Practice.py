# 绘制图形
# 2.14
import turtle

# x1, y1 = eval(input("input tow number for x1 and y1"))
# x2, y2 = eval(input("input tow number for x2 and y2"))
# length = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
# turtle.showturtle();
# turtle.penup();
# turtle.goto(x1, y1)
# turtle.write(str(x1) + "," + str(y1))
# turtle.pendown()
# turtle.goto(x2, y2)
# turtle.write(str(x2) + "," + str(y2))
#
# centerPotX = (x1 + x2) / 2
# centerPotY = (y1 + y2) / 2
# turtle.penup
# turtle.goto(centerPotX, centerPotY)
# turtle.pendown()
# turtle.write(length)
# turtle.done()

# 2.7 用户输入时间，计算年月日
# secondAll = eval(input("please input a second time"))
# second = secondAll % 60
#
# minuteAll = secondAll // 60
#
# minute = minuteAll % 60
#
# hourAll = minuteAll // 60
#
# hour = hourAll % 24
#
# day = hourAll // 24
#
# print(hour, minute, second)

# 2.1  计算银行利率
# money = eval(input("please input money"))
# percent = eval(input("please input percent"))
# year = eval(input("please input year"))
# deposit = money / ((1 + percent) ** (year))
# print(deposit)


# 2.19
amount = eval(input("please input amount"))
percent = eval(input("please input persent"))
year = eval(input("please input year"))

allAmount = amount * ((1 + percent) ** year)
print(allAmount)
