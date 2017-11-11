import threading
import time
def run(n):
    lock.acquire()#加锁，保证同一时刻只有一个线程使用
    global num#把num变成全局变量的那个num
    num+=1
    time.sleep(0.5)
    lock.release()

lock = threading.Lock()
num = 0
t_obj = []#存线程实例
for i in range(50):
    t = threading.Thread(target=run,args=('t-%s'%i,))
    t.start()
    t_obj.append(t)

for t in  t_obj:
    t.join()

print('-----all threads has finish...',threading.current_thread())

print('num:',num)