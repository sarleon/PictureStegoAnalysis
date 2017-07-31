#coding:utf-8
import random,commands,re
from output_helper import color_print,debug_log
import os
from config import base_path,tmp_path





"""
每一个module从Base
"""
class BaseModule():

    # 需要的系统程序命令
    requirement = None

    # 模块名字
    name = "Base Module"


    desribtion = ""


    def __init__(self):
        color_print("[模块:"+self.name+"],"+self.desribtion,1)


    def module_print(self,content):
        color = random.uniform(2,9)
        res = "["+self.name+"]: "+content
        color_print(res,color)


    """
    模块运行之前的检查
    """
    def pre_check(self):

        if self.requirement !=None:
            if not self.exist():
                color_print("["+self.name+"]"+"system command "+self.requirement+" not found ,please check if the requirement is installed",1)
                return False




    def exist(self):
        result = commands.getoutput(self.requirement)
        pattern = re.compile('not found')
        if pattern.search(result):
            return False
        else:
            return True


    """
    每一个从BaseModule继承的类都应该重写run方法
    """
    def run(self,filename,content=None):
        raise NotImplementedError





class ExifModule(BaseModule):
    requirement = 'exif'
    name = 'exif 模块'
    desribtion = "检查jpg/jpeg格式文件的exif信息"
    def run(self,filename,content=None):
        result = commands.getoutput("exif "+filename)
        self.module_print(result)


class BinwalkModule(BaseModule):
    requirement = 'binwalk'
    name = 'binwalk 模块'
    desribtion =  '检查二进制文件的类型'
    def run(self,filename,content=None):
        result = commands.getoutput("binwalk "+filename)
        self.module_print(result)

class ForemostModule(BaseModule):
    requirement = 'foremost'
    name = 'foremost模块'
    desribtion = "从二进制文件中分离出"
    def run(self,filename,content=None):


        result = commands.getoutput("foremost -o "+tmp_path+" "+filename )


        commands.getoutput('rm -rf '+tmp_path)




enable_module_list=[BinwalkModule,ExifModule,ForemostModule]