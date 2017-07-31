import commands,re
from output_helper import color_print,debug_log
class BaseModule():
    def __init__(self,requirement):
        self.requirement= requirement

    def pre_check(self):

        if self.requirement !=None:
            if not self.exist():
                color_print("system command "+self.requirement+" not found ,please check if the requirement is installed",1)
                return False




    def exist(self):

        result = commands.getoutput(self.requirement)
        pattern = re.compile('not found')
        if pattern.search(result):
            return False
        else:
            return True









