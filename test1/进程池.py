from multiprocessing import Process,Pool,freeze_support
import time,os

def Foo(i):
    time.sleep(1)
    print('in process',os.getpid())
    return i + 100

def Bar(arg):
    print('-->exec done:',arg,os.getpid())

if __name__ == '__main__':
    # freeze_support()#没有这个，window下运行会报错
    pool = Pool(processes=5)#允许进程池同时放入5个进程
    print('主进程',os.getpid())
    for i in range(10):
        pool.apply_async(func=Foo, args=(i,), callback=Bar)#callback=回调,可以主进程连数据库，子进程写日志，这样就不用子进程连数据库并且写日志了
        # pool.apply(func=Foo, args=(i,))#同步执行，也就是串行
        # pool.apply_async(func=Foo,args=(i,))#并行

    print('end')
    pool.close()
    pool.join()#进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭