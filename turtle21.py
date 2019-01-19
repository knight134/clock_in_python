# -*-coding:utf8 -*-
import turtle

ninjia=turtle.Turtle()

ninjia.speed(10)

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

    ninjia.right(2)

turtle.done()