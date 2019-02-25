#!/usr/bin/python
# -*-coding:utf8 -*-
__author__="wanglongfei"

'''
    计算基础代谢率 Basal metabolic rate
    加入可try except: 错误捕获代码
'''
def main():
    flag = input("是否退出程序（y/n）")
    # weight=float(input("体重（kg）:"))
    # height=float(input("身高（cm）："))
    # age=int(input("年龄："))
    # gender=input("性别：")
    # flag=input("是否退出程序（y/n）")
    while (flag != "y"):
        print("请输入以下信息用空格分隔")
        input_str=input("请输入您的性别，身高cm，体重kg，年龄：")
        arr=input_str.split(" ")
        try:
            weight=float(arr[2])
            height=float(arr[1])
            age=int(arr[3])
            gender=arr[0]
            # while(flag!="y"):
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
            # flag=input("是否退出程序（y/n）")
        except(ValueError):
            print("请输入正确的信息！")
        except(IndexError):
            print("请输入正确的信息！")
        except:
            print("程序异常")
        flag = input("是否退出程序（y/n）")
        try:
            if(bmr):
                print("最后一次bmr为："+str(bmr))
        except:
            print("变量bmr未定义")


if(__name__=="__main__"):
    main()
