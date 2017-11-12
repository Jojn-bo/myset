#pycharm有一个线程，启动'get_进程.py'这个进程，然后代码启动的进程的父进程id是‘get_进程.py’这个进程
from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())#父进程
    print('process id:', os.getpid())#子进程
    print('\n\n')

def f(name):
    info('\033[31;1mcalled from child process function f\033[0m')
    print('hello',name)

if __name__ == '__main__':
    info('\033[32;1mmain process line\033[0m')
    p = Process(target=f, args=('bob',))
    p.start()
    # p.join()