import time,random,queue,threading

q = queue.Queue()
def Produce(name):
    count = 0
    while count < 20:
        time.sleep(random.randrange(3))
        q.put(count)
        print('Producer %s has produced %s 包子...'%(name,count))
        count += 1

def Consumer(name):
    count = 0
    while count < 20:
        time.sleep(random.randrange(4))
        if not q.empty():
            data = q.get()
            print(data)
            print('\033[32;1mConsumer %s has eat %s 包子...\033[0m'%(name,data))
        else:
            print('-----no 包子 anymore-----')
        count += 1

p1 = threading.Thread(target=Produce, args=('A',))
c1 = threading.Thread(target=Consumer, args=('B',))
p1.start()
c1.start()