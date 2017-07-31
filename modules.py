#coding:utf-8
import random,commands,re
from output_helper import color_print,debug_log






"""
每一个module从Base
"""
class BaseModule():

    # 需要的系统程序命令
    requirement = None

    # 模块名字
    name = "Base Module"


    desribtion = "Base Class of all the modules"


    def __init__(self):
        pass


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
    name = 'exif module'
    def run(self,filename,content=None):
        result = commands.getoutput("exif "+filename)
        self.module_print(result)



enable_module_list=[ExifModule]