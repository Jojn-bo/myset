#类似与管道的东西
from multiprocessing import Process, Pipe

def f(conn):
    conn.send([42,None,'hello from child'])
    conn.send([42, None, '你好，父进程'])
    print('from parent:',conn.recv())
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()#管道生成两个对象
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    print(parent_conn.recv())
    parent_conn.send('你好，子进程')
    p.join()