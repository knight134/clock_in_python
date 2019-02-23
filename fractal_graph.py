#!/usr/bin/python
# -*-coding:utf8 -*-

__author__="wanglongfei"

import turtle
'''
    完成一个分形树的绘制
    使用递归函数
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
    def draw_recursive_pentagram(self,size):
        '''
        迭代绘制五角星
        :param size:
        :return:
        '''
        count=1
        while(count<=5):
            turtle.forward(size)
            turtle.right(144)
            count=count+1

        size=size+10
        if(size<=100):
            self.draw_recursive_pentagram(size)
    def fractal_tree(self,branch_length):
        '''
        绘制分形树的函数
        :param branch_length:
        :return:
        '''
        if(branch_length>3):
            if(branch_length<30):
                turtle.pencolor("green")
                turtle.pensize(1)
            else:
                turtle.pensize(2)
                turtle.pencolor("black")
            turtle.forward(branch_length)
            turtle.right(20)
            self.fractal_tree(branch_length-18)
            # 准备绘制左侧树
            turtle.left(40)
            self.fractal_tree(branch_length-18)
            # 返回
            turtle.right(20)
            turtle.penup()
            turtle.backward(branch_length)
            turtle.pendown()


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
    turtle.left(90)
    turtle.backward(400)
    turtle.pendown()
    turtle.pensize(1)
    turtle.pencolor("red")

    # while(size<=100):
    #     p.pentagon(size)
    #     # size = size + 10
    #     size+=10
    # p.draw_recursive_pentagram(50)
    turtle.speed(0)
    p.fractal_tree(150)
    turtle.exitonclick()
