#!/usr/bin/python
# -*-coding:utf8 -*-
import os

__author__="knight"

import sys
import json
import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd

'''
    空气质量指数 (AQI air quality index)
    各指标线性缩放然后取最大值
    从网站pm25.in实时获取数据
    获取所有城市的aqi
    爬取的所有数据保存为csv文件
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
class Spider():
    def __init__(self):
        self.url=""
    def run(self):
        #city=input("请输入城市拼音：")
        self.url="http://pm25.in/"
        url_text=self.get_html_text()
        print(url_text)
        #aqi=self.get_aqi(url_text)
        #print(aqi)
        cities=self.get_all_cities(url_text)
        for c in cities:
            aqi=self.get_city_aqi(c[1])
            print(c[0]+"\t"+str(aqi))

    def get_html_text(self):
        r=requests.get(self.url,timeout=30)
        #print(r.status_code)
        return r.text
    def get_city_aqi(self,city_pinyin):
        url="http://pm25.in/"+city_pinyin
        url_text = self.get_html_text()
        return self.get_aqi(url_text)

    def get_aqi(self,text):
        b=BeautifulSoup(text,"lxml")
        div_list=b.find_all('div',{'class':'span1'})
        info=[]
        for i in range(8):
            div_content=div_list[i]
            caption=div_content.find('div',{'class':'caption'}).text.strip()
            value=div_content.find('div',{'class':'value'}).text.strip()
            info.append((caption,value))
        return info
    def get_all_cities(self,text):
        '''
        获取所有城市列表
        :return:
        '''
        city_list=[]
        b = BeautifulSoup(text, "lxml")
        city_div=b.find_all("div",{'class':'bottom'})[1]
        city_link_list=city_div.find_all('a')
        for city_link in city_link_list:
            city_name=city_link.text
            city_pinyin=city_link['href'][1:]
            city_list.append((city_name,city_pinyin))
        return city_list
    def write_data(self):
        header=["city","AQI","PM2.5","PM10","CO","NO2","O3","O3/8h","SO2"]
        with open("city_aqi.csv","w",encoding="utf-8",newline="") as f:
            writer=csv.writer(f)
            writer.writerow(header)
            for i,city in enumerate(city_list):
                city_name=city[0]
                city_pinyin=city[1]
                city_aqi=self.get_city_aqi(city_pinyin)
                row=[city_name]+city_aqi
                writer.writerow(row)
class Analysis():
    def __init__(self):
        pass
    def read_csv(self,file):
        self.aqi_data=pd.read_csv(file)
        print(self.aqi_data["city"])
        print(self.aqi_data[["city","aqi"]])
        
if(__name__=="__main__"):
    a=AQI()
    '''
    aqi=a.test_data()
    aqi.sort(key=lambda city:city['aqi'],reverse=True)
    print(aqi)
    AQI.write_data(aqi,"aqi_out.json")
    '''
    s=Spider()
    s.run()