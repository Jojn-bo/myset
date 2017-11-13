import queue

# q = queue.LifoQueue()
#
# q.put(1)
# q.put(2)
# q.put(3)
#
# print(q.get())
# print(q.get())
# print(q.get())

q = queue.PriorityQueue()

# q.put(('chenronghua',-1))#安装字母排序
q.put((10,'alex'))
q.put((-1,'hanyang'))
q.put((3,'wangsen'))

print(q.get())
print(q.get())
print(q.get())


