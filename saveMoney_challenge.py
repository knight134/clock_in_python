#!/usr/bin/python
# -*-coding:utf8 -*-
import datetime
'''
52周存钱挑战
输入一个日期，判断是第几周，然后输出该周的存款金额
'''
import math
def main():
    """
        主函数
    :return:
    """
    money_per_week=10 # 初始化每周存入金额
    i=1    # 初始化周数
    increase_money=10 # 每周递增的钱数
    total_week=52     # 总共52周

    saving=0          # 账户累计钱数
    money_list=[]
    saving_list=[]     # 每周累计存钱数
    # while 循环
    while(i<=total_week):
        #saving=saving+money_per_week
        # 更新下一周的存钱金额
        # money_per_week=money_per_week+increase_money
        # i=i+1
        money_list.append(money_per_week)
        saving=math.fsum(money_list)
        saving_list.append(saving)

        # 输出信息
        print("第{}周，存入{}元，账户累计{}元".format(i,money_per_week,saving))
        # money_list.append(money_per_week)

        money_per_week = money_per_week + increase_money
        i = i + 1

    ###################
    date=input("请输入日期：(yy/m/d)")
    week=datetime.datetime.strptime(date,"%Y/%m/%d").isocalendar()[1]
    print("该日期周数："+str(week))
    print("第"+str(week)+"周，存入"+str(money_list[week-1])+"元，账户累计"+str(saving_list[week-1])+"元")
if(__name__=="__main__"):
    main()