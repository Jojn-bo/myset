#用队列和线程来实现
import threading,time,queue

q = queue.Queue(maxsize=10)#队列的最大数量

def Producer(name):
    while True:
        count = 1
        for count in range(10):
            q.put('骨头%s'%count)
            print('生成了骨头',count)
            count += 1
            time.sleep(0.5)


def Consumer(name):
    #while q.qsize()>0:
    while True:
        print('[%s] 取到 [%s] 并且吃了它。。。'%(name, q.get()))
        time.sleep(1)

p = threading.Thread(target=Producer,args=('Alex',))
c = threading.Thread(target=Consumer,args=('ChengRonghua',))
c1 = threading.Thread(target=Consumer,args=('王',))

p.start()
c.start()
c1.start()