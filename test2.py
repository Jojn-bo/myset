#列表嵌套字典
list=[]
dir={}
x=0
while x < 5:
    dir['name']=input('name=')
    dir['age']=input('age=')
    list.append(dir.copy())
    x+=1

# list1=[{'name':'a','age':9},{'name':'b','age':10}]

for x in list:
    flag =input('nums=')
    print(x.get('flag'))

# while x < len(list):
#     dir1={list[x]}
#     dir1.get()
#     x+=1

