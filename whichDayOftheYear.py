#!/usr/bin/python
# -*-coding:utf8 -*-

__author__="wanglongfei"
__version__="1.0"

import sys
import os
import time
import datetime

'''
    输入某年某月某日，判断这一天是这一年的第几天？
    四年一润，百年不润，四百年一润
'''

class WhichDay():
    def __init__(self):
        self.days_in_month_tup=(31,28,31,30,31,30,31,31,30,31,30,31)
    def set_input(self):
        input_date_str=input("请输入如期（yyyy/mm/dd）:")
        self.input_date=datetime.datetime.strptime(input_date_str,"%Y/%m/%d")
        print(self.input_date)

        self.year=self.input_date.year
        self.month=self.input_date.month
        self.day=self.input_date.day
    def days(self):
        sum_days=sum(self.days_in_month_tup[:self.month-1])+self.day
        # 如果是闰年需要额外的处理
        if(self.year%400==0 or(self.year%4==0 and self.year%100!=0)):
            if(self.month>2):
                sum_days=sum_days+1
        # 输出日期
        print("一年中的第"+str(sum_days)+"天")
if(__name__=="__main__"):
    w=WhichDay()
    w.set_input()
    w.days()