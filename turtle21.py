# -*-coding:utf8 -*-
import turtle

ninjia=turtle.Turtle()

ninjia.speed(10)
# 每次刷新的间隔时间

for i in range(180):
    ninjia.forward(100)
    ninjia.right(30)
    ninjia.forward(20)
    ninjia.left(60)
    ninjia.forward(50)
    ninjia.right(30)

    ninjia.penup()
    ninjia.setposition(0,0)
    ninjia.pendown()
    # 一系列底层绘图函数
    ninjia.right(2)

turtle.done()
