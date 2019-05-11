#!/usr/bin/python
# -*-coding:utf8 -*-
import os

__author__="knight"

import sys
import json

'''
    空气质量指数 (AQI air quality index)
    各指标线性缩放然后取最大值
'''
'''
    json操作
    dumps()
    loads()
    dump() python数据对象写入到json文件
    load()
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
        pass
    def aqi_co(self,val):
        pass
    def cal_aqi(self):
        return(max(self.result))
    @staticmethod
    def liner(a,b,c,d,x):
        '''
        计算线性缩放值
        :param a:
        :param b:
        :param c:
        :param d:
        :param x:
        :return:
        '''
        return ((x-c)/(d-c))*(b-a)+a
    def test_data(self):
        f=open("aqi1.json",encoding="utf-8")
        j=json.load(f)
        f.close()
        self.data1=j

        return j
    @staticmethod
    def write_data(obj,outfile):
        fout=open(outfile,"w",encoding="utf8")
        json.dump(obj,fout,ensure_ascii=False)
        fout.close()
if(__name__=="__main__"):
    a=AQI()
    aqi=a.test_data()
    aqi.sort(key=lambda city:city['aqi'],reverse=True)
    print(aqi)
    AQI.write_data(aqi,"aqi_out.json")