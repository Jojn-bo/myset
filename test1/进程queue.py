from multiprocessing import Process, Queue

def f(qq):
    qq.put([42, None, 'hello'])

if __name__ == '__main__':
    q = Queue()

    # 进程queue放进子进程中，可以被父进程访问，而单独的import queue中的queue则不行
    p = Process(target=f, args=(q,))
    p.start()#启动父进程带出的子进程

    print(q.get())#print('[42, None, 'hello']')，这个是父进程执行的print
    p.join()
