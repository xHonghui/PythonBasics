# 绘制 stop 牌
import turtle

turtle.showturtle()
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.circle(100, steps=6)
turtle.end_fill()

turtle.penup()
turtle.goto(-50, 0)
turtle.pendown()
turtle.color("white")
turtle.write("STOP", font=("Times", 30, "bold"))
turtle.hideturtle()

turtle.done()
