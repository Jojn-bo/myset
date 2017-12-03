#1.先把整体的框架考虑清楚
#1.1提示用户选择功能
#放入函数中,并提示用户选择功能
def showInfo():
    print("-"*20)
    print("   学生管理系统   ")
    print("1:添加学生信息")
    print("2:删除学生信息")
    print("3:修改学生信息")
    print("4:查询学生信息")
    print("5:退出")
    print("-"*20)
    key=int(input("请选择功能（序号）："))
    return key

#1.3功能函数
student={}                      #学生个人信息
studentList=[]                  #学生全部信息

#添加学生信息
def addStudent():
    student["name"]=input("请输入学生的姓名：")
    student['age']=int(input('请输入学生的年龄：'))
    studentList.append(student.copy())

#删除学生信息
def delStudent():
    flag=input('请输入删除学生的名字：')
    for x in studentList:
        i=0
        if flag == x.get('name'):
            print('成功查找到，执行删除')
            studentList.pop(i)
        i+=1



#修改学生信息
def modStudent():
    pass

#查询学生信息
def queStudent():
    for x in studentList:
        print(x)

#推出系统
def ex():
    exit()

#1.4执行功能
def execution(key):
    if key ==1:
        addStudent()
    elif key==2:
        delStudent()
    elif key==3:
        modStudent()
    elif key==4:
        queStudent()
    elif key==5:
        ex()
    else:
        print("您的输入不合规范，请重新输入！")


while True:
    keys=showInfo()
    execution(keys)
