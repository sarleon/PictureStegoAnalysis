#coding:utf-8
from output_helper import print_banner,common_print,time_print,color_print
from modules import enable_module_list
import sys

def main():
    print_banner()
    if len(sys.argv)<2:
        color_print("please input the path of the picture as the first argument")
        return
    filename = sys.argv[1]
    file = open(filename,'rb').read()

    for Module in enable_module_list:

        module = Module()
        module.run(filename,file)






if __name__ == '__main__':
    main()
