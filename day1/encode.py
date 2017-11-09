import  sys
import time
print(sys.getdefaultencoding())#打印系统默认字符编码
s = '你好'
y = s.encode()#utf-8 编码成 bytes
print(y,type(y))
z = y.decode()#bytes 解码成 utf-8
print(z,type(z))

time1 = '%Y %m %d '
print('test')