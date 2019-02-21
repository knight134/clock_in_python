#!/usr/bin/python
# -*-coding:utf8 -*-

__author__="wanglongfei"

import turtle
'''
    完成一个分形树的绘制
'''

class Pentagram():
    '''
        五角星形的绘制
        turtle.forward(distance)
        turtle.backward(distance)
        turtle.right(degree)
        turtle.left(degree)

    '''
    def __init__(self):
        pass
    def show(self):
        turtle.forward(300)
        turtle.right(60)
        turtle.backward(250)

        turtle.exitonclick()
    def pentagon(self,size):
        for i in range(5):
            turtle.forward(size)
            turtle.right(144)
        #turtle.exitonclick()

'''
    turtle.penup() 抬起画笔，之后移动画笔不绘制图形
    turtle.pendown() 落下画笔
    turtle.pensize()
    turtle.pencolor()
        white black grey darkgreen gold violet purple 
'''

if(__name__=="__main__"):
    p=Pentagram()
    p.pentagon(200)
    p.pentagon(150)
    size=50
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor("red")

    while(size<=100):
        p.pentagon(size)
        # size = size + 10
        size+=10
    turtle.exitonclick()
