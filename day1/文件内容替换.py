# f = open('霸王别姬','r',encoding='utf-8')
# f_new = open('霸王别姬2','w',encoding='utf-8')

# with open('霸王别姬','r',encoding='utf-8') as f:#用with打开文件
#     with open('霸王别姬2','w',encoding='utf-8') as f_new:
#         for i in f:
#             if '我' in i:
#                 i = i.replace('我', '成')
#             f_new.write(i)
import sys
print(sys.getdefaultencoding())

with open('霸王别姬','r',encoding='utf-8') as f, \
        open('霸王别姬2','w',encoding='utf-8') as f_new:
    for i in f:
        if '我' in i:
            i = i.replace('我', '成')
        f_new.write(i)


# f.close()
# f_new.close()