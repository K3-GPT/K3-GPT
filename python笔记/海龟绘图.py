import turtle

# 创建海龟对象
t = turtle.Turtle()

# 更改画布颜色为红色
t.bgcolor("red")

# 移动海龟
t.forward(100)  # 向前移动100个像素
t.backward(50)  # 向后移动50个像素
t.right(90)  # 向右转90度
t.left(45)  # 向左转45度

# 抬起画笔，不作图
t.penup()

# 移动海龟到新的位置
t.goto(100, 100)

# 改变画笔颜色和粗细
t.color("red")  # 设置画笔颜色为红色
t.pensize(6)  # 设置画笔粗细为2个像素

# 绘制形状
t.circle(50)  # 画一个半径为50的圆
t.dot(20, "blue")  # 画一个蓝色的直径为20的点

# 控制海龟的显示和隐藏
t.hideturtle()  # 隐藏海龟
t.showturtle()  # 显示海龟

# 清空画布
t.clear()  # 清空画布上的所有内容

# 控制海龟的速度
t.speed(12)  # 设置海龟移动速度为最慢
t.speed(0)  # 设置海龟移动速度为最快

# 绘制完成后显示绘图窗口
turtle.done()
