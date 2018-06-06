import turtle
# 绘制三角形
turtle.screensize(1080, 1920)
turtle.showturtle()
turtle.penup()
turtle.goto(-100, -200)
turtle.pendown()
turtle.pensize(3)
turtle.begin_fill()
turtle.color("red")
turtle.circle(30, steps=3)
turtle.end_fill()

# 撤销之前绘制的图形
# turtle.reset()

# 绘制正方形
turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.begin_fill()
turtle.color("blue")
turtle.circle(40, steps=4)
turtle.end_fill()

# 绘制五边形
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.begin_fill()
turtle.color("green")
turtle.circle(40, steps=5)
turtle.end_fill()

# 绘制六边形
turtle.penup()
turtle.goto(50, 50)
turtle.pendown()
turtle.begin_fill()
turtle.color("purple")
turtle.circle(40, steps=6)
turtle.end_fill()

# 绘制实心圆形
turtle.penup()
turtle.goto(150, 100)
turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.circle(50)
turtle.end_fill()

# 绘制标题文字
turtle.penup()
turtle.goto(-100,200)
turtle.pendown()
turtle.color("purple")
turtle.write("Cool Colorful Shaps",font = ("Times",20,"bold"))
turtle.hideturtle()
turtle.done();
