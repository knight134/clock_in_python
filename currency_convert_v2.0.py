# -*-coding:utf8 -*-
__author__="wanglongfei"
'''
    程序可以一直运行，直到用户选择退出
'''
# 汇率
USD_VS_RMB=6.77

currency_str_value=input("请输入带单位的货币金额（退出程序请输入Q）：")
print(currency_str_value)
i=0
while(currency_str_value!="Q"):
    # 提取字符串中的数值，单位。将美元转为人民币，将人民币转为美元
    unit=currency_str_value[-3:]
    print(unit)

    if(unit=='CNY'):
        rmb_str_value=currency_str_value[0:-3]
        rmb_value=eval(rmb_str_value)
        usd_value=rmb_value/USD_VS_RMB
        print("美元（USD）金额是：",usd_value)
    elif(unit=="USD"):
        usd_str_value=currency_str_value[:-3]
        usd_value=eval(usd_str_value)
        rmb_value=usd_value*USD_VS_RMB
        print("人民币（CNY）金额是：",rmb_value)
    else:
    # 其它情况
        print("该程序目前版本尚不支持该种货币！")
    print("####################################")
    currency_str_value=input("请输入带单位的货币金额（退出程序请输入Q）：")
    i=i+1
    print("循环次数",i)
print("程序已经退出")