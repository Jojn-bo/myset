#单线程下的多路复用
import select
import socket
import queue

server = socket.socket()#实例化
server.bind(('localhost',9000))#绑定地址
server.listen(1000)#监听1000个端口

server.setblocking(False)#设置为非阻塞模式

inputs = [server,]
outputs = []

readable,writeable,exceptional = select.select(inputs, outputs, inputs)#第一个
print(readable,writeable,exceptional)
for r in readable:
    conn,addr = server.accept()
    print(conn,addr)