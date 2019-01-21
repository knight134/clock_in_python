# -*-coding:utf8 -*-
'''
    汇率换算程序
    将人民币换算成美元，或者将美元换算成人民币
'''
# eval() 函数用来执行一个字符串表达式，并返回表达式的值
__version__="1.0"
__author__="小象"

rmb_value=input("请输入人民币（CNY）金额：")
print(rmb_value)
usd_rmb=6.77

usd=int(rmb_value)/usd_rmb
print("美元（USD）金额是："+str(usd))
