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
                color_print("["+self.name+"]"+"软件 "+self.requirement+"未找到或添加到环境变量中,",1)
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

class FoundementalCheckModule(BaseModule):
    requirement = None
    name = "基本检查"
    desribtion = "一些基本的检查"



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
        tmp_files = os.listdir(tmp_path)
        file_type_num = len(tmp_files) - 1
        total_files = []
        for diretory in tmp_files:
            if diretory != 'audit.txt':
                dir_path = tmp_path+diretory
                sub_dir_files = os.listdir(dir_path)
                map(total_files.append,[dir_path+os.path.sep+sub_dir_file for sub_dir_file in sub_dir_files])
        n = len(total_files)
        if n>1:
            self.module_print("共分离出了%d个文件,文件名为"%n)
            for file_path in total_files:
                os.system("mv %s PSA-Foremost-%s"%(file_path,file_path))
                color_print("PSA-Foremost-%s"%file_path,5)
        else:
            self.module_print("仅分离出一个文件")
            origin_size = os.path.getsize(filename)
            self.module_print("源文件的大小为%d"%origin_size)
            cur_size = os.path.getsize(total_files[0])
            self.module_print("分离出的文件的大小为%d"%cur_size)
            if origin_size>cur_size:
                self.module_print("源文件的大小大于分离出的文件的大小,源文件中可能存在隐藏信息")
            f_origin = open(filename,'rb')
            f_origin.seek(cur_size)
            data = f_origin.read()
            self.module_print("从尾部提取出的可能的隐藏信息是")
            color_print("********************************上分割线**********************************",6)
            color_print(data,4)
            color_print("********************************下分割线**********************************",6)


        commands.getoutput('rm -rf '+tmp_path)





enable_module_list=[BinwalkModule,ExifModule,ForemostModule]