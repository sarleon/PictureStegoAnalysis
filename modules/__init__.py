#coding:utf-8
import commands,re
from output_helper import color_print,debug_log
class BaseModule():
    def __init__(self,requirement):

        self.requirement= requirement
        self.name = "Base Module"

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









