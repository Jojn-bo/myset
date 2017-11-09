f = open('霸王别姬','r',encoding='utf-8')
# date = f.read()
# date2 = f.read()
# print(date)
# print(50*'-',date2)
# f.write(50*'+')
# print(f)

# for index,i in enumerate(f.readlines()):
#     print(i.strip())

#循环读取文件
count = 0
for line in f:
    if count == 9:
        print('-----------------------------')
    print(line)
    count+=1



print(f.tell())#打印文件指针的位置，按字符数
f.seek(0)#把文件指针放到指定位置
print(f.encoding)#打印给模块的使用什么编码的
print(f.fileno())#打印文件描述符
print(f.flush())#刷新缓存
f.truncate(80)#截断，从头开始截断X个字符