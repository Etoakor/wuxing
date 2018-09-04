import turtle
import time


turtle.setup(width=0.9, height=0.9)
# width, height,输入宽和高为整数时, 表示像素; 为小数时, 表示占据电脑屏幕的比例
turtle.bgcolor("red")           # 画布背景颜色
turtle.fillcolor("yellow")      # 绘制图形的填充颜色
turtle.color('yellow')          # 绘制图形颜色
turtle.speed(10)                # 绘制图形的速度

# 主星
turtle.begin_fill()# 准备开始填充图形
turtle.up()
turtle.goto(-600, 220)  # 将画笔移动到坐标为-600, 220的位置
turtle.down()
for i in range(5):
    turtle.forward(150)  # 向当前画笔方向移动150像素长
    turtle.right(144)# 顺时针移动 144°
turtle.end_fill()        # 填充完成
time.sleep(1)

# 第1颗副星
turtle.begin_fill()
turtle.up()
turtle.goto(-400, 295)
turtle.setheading(305)
turtle.down()
for i in range(5):
    turtle.forward(50)
    turtle.left(144)      # 逆时针移动 144°
turtle.end_fill()
time.sleep(1)


# 第2颗副星
turtle.begin_fill()
turtle.up()
turtle.goto(-350, 212)
turtle.setheading(30)
turtle.down()
for i in range(5):
    turtle.forward(50)
    turtle.right(144)
turtle.end_fill()
time.sleep(1)

# 第3颗副星
turtle.begin_fill()
turtle.up()
turtle.goto(-350, 145)
turtle.setheading(5)
turtle.down()
for i in range(5):
    turtle.forward(50)
    turtle.right(144)
turtle.end_fill()
time.sleep(1)

# 第4颗副星
turtle.begin_fill()
turtle.up()
turtle.goto(-400, 90)
turtle.setheading(300)
turtle.down()
for i in range(5):
    turtle.forward(50)
    turtle.left(144)
turtle.end_fill()
time.sleep(10)