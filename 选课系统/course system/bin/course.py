import sys,os

#获取course system的目录地址
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#添加进环境变量
sys.path.append(BASE_DIR)

from core import main

if __name__ == '__main__':
    a = main.Run()
    a.interactive()
