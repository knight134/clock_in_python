#!/usr/bin/python
# -*-coding:utf8 -*-
__author__="knight"

import sys

'''
    空气质量指数 (AQI air quality index)
    各指标线性缩放然后取最大值
'''
class AQI():
    def __init__(self):
        self.aqi=0
        self.result=[]
        # 多个分类指标的计算值放到一个数组中。
    def detect(self):
        print("请输入以下信息，用空格分隔")
        input_str=input("(1)PM2.5 (2)CO:")
        str_list=input_str.split(" ")
        pm_val=float(str_list[0])
        co_val=float(str_list[1])

        self.param_list=[]
        self.param_list.append(pm_val)
        self.param_list.append(co_val)
    def aqi_pm(self,val):
    def aqi_co(self,val):
    def cal_aqi(self):
        return(max(self.result))

