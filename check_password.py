#!/usr/bin/python
# -*-coding:utf8 -*-
import os

class PasswordTool():
    def __init__(self,password):
        self.password=password
        self.strength_level=0
    def process_password(self):
        if(self.check_length()):
            self.strength_level+=1
        else:
            print("密码长度不足6位")
        if(self.check_alpha()):
            self.strength_level+=1
        else:
            print("密码没有包含字母")
        if(self.check_number()):
            self.strength_level+=1
        else:
            print("密码没有包含数字")
    def check_length(self):
        flag=False
        if(len(self.password)>=6):
            flag=True
        return flag

    def check_number(self):
        has_number=False
        for c in self.password:
            if(c.isnumeric):
                has_number=True
                break
        return has_number
    def check_alpha(self):
        has_letter=False
        for c in self.password:
            if(c.isalpha()):
                has_letter=True
                break
        return has_letter

class FileTool():
    '''
        文件的读取
        文件的写入
    '''
    def __init__(self,filepath):
        self.filepath=filepath
    def write_to_file(self,line):
        f=open(self.filepath,"a")
        f.write(line)
        f.close()
    def read_from_file(self):
        f=open(self.filepath,"r")
        lines=f.readlines()
        f.close()
        return lines
def main():
    total_times=5
    filepath="password.txt"
    file_tool=FileTool(filepath)
    while(total_times>0):
        password=input("请输入密码：")
        password_tool=PasswordTool(password)
        password_tool.process_password()

        line="密码："+password_tool.password+"\t强度："+str(password_tool.strength_level)+"\n"
        file_tool.write_to_file(line)

        if(password_tool.strength_level==3):
            print("恭喜，密码强度合格！")
            break
        else:
            print("密码强度不合格")
            total_times-=1


        if(total_times<=0):
            print("尝试次数过多，密码设置失败！")

    print(file_tool.read_from_file())

if(__name__=="__main__"):
    main()