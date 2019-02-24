#!/usr/bin/python
# -*-coding:utf8 -*-
__author__="wanglongfei"

'''
    计算基础代谢率 Basal metabolic rate
    
'''
def main():
    weight=float(input("体重（kg）:"))
    height=float(input("身高（cm）："))
    age=int(input("年龄："))
    gender=input("性别：")
    flag=input("是否退出程序（y/n）")

    while(flag!="y"):
        #bmr=0
        if(gender=="男"):
            bmr=13.7*weight+5.0*height-6.8*age+66
        elif(gender=="女"):
            bmr=9.6*weight+1.8*height-4.7*age+655
        else:
            bmr=-1
        # bmr 注意变量的作用域有点古怪
        if(bmr!=-1):
            print("基础代谢率（大卡）："+str(bmr))
        else:
            print("暂不支持该性别！")
        flag=input("是否退出程序（y/n）")
    print("最后一次bmr为："+str(bmr))


if(__name__=="__main__"):
    main()
