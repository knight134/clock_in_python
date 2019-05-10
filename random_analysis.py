#!/usr/bin/python
# -*-coding:utf8 -*-
'''
    模拟随机事件，投骰子
'''
import random
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

def roll_dice():
    roll=random.randint(1,6)
    return roll

def main():
    total_times=10000
    result_list=[0]*11
    roll_list=list(range(2,13))
    roll_dict=dict(zip(roll_list,result_list))

    roll_list1=[]
    roll_list2=[]
    roll_sum=[]
    for i in range(total_times):
        roll=roll_dice()
        roll1=roll_dice()
        roll_list1.append(roll)
        roll_list2.append(roll1)
        roll_sum.append(roll+roll1)

        '''
        for j in range(1,7):
            if(roll==j):
                result_list[j-1]+=1
        #print(roll_dice())
        '''
        roll_dict[roll+roll1]+=1
    #print(result_list)
    '''
    for (i,result) in enumerate(result_list):
        print("点数："+str(i+1)+"\t次数："+str(result)+"\t频率："+str(result/total_times))
    '''
    x=range(1,total_times+1)
    plt.scatter(x,roll_list1,alpha=0.4,c="red")
    plt.scatter(x,roll_list2,alpha=0.4,c="green")
    plt.show()
    # 直方图对数据进行简单分析
    # 对数据进行分组，统计每个分组内的数据的数量
    plt.hist(roll_sum,bins=range(2,14),edgecolor="green",linewidth=1,normed=1)
    plt.title("骰子点数统计")
    plt.xlabel("点数")
    plt.ylabel("频率")
    plt.show()
    for i,result in roll_dict.items():
        print("点数：" + str(i) + "\t次数：" + str(result) + "\t频率：" + str(result / total_times))
if(__name__=="__main__"):
    main()