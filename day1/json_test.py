import json

a = 'asd'
b = {1: 'a', 2: 'b','c':'d'}

# c = json.dumps(b)
# print(c)
# # print(c['c'])#错误
# d = json.loads(c)
# print(d['c'])

c = json.dumps(b).encode()
print(c)
d = json.loads(c)#不需要decode（）
print(d)
print(d['c'])