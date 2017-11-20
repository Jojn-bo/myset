#客户端
import socket

client = socket.socket()#声明socket类型，同时生成socket链接对象
client.connect(('localhost',10001))

while True:
    msg = input('>>:').strip()
    if len(msg) == 0:
        continue
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode())

client.close()
