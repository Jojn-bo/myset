class home:
    def __init__(self):
        self.area = 180         #家的大小
        self.furniture = []     #家具的列表
        self.lighting = 'off'  #家里的光照亮度

    def __str__(self):
        msg = '这是我的家'+'\n'+'家里有'
        for temp in self.furniture:
            msg = msg + temp +','
        msg=msg.strip(',')
        msg+='\n' + '家里很'
        if self.lighting == 'off':
            msg+='暗'
        else:
            msg+='亮'
        return msg

    def __del__(self):
        pass
    
    def setFurniture(self,furniture):
        self.name = furniture.getName()
        self.size = furniture.getSize()
        self.furniture.append(self.name)

        msg='我向家里运了一个'+self.name
        print(msg)
        if self.area >= self.size:
            self.area-=self.size
            print('可以放下这个家具，家里的面积还有',self.area)
        else:
            print('东西太大了，放不下')

    def lightStatus(self,flag):
        if flag == 1:
            self.lighting = 'on'
        else:
            self.lighting = 'off'

class furniture(object):
    def __init__(self,name,size):
        self.name = name
        self.size = size

    def __str__(self):
        msg='我是'+self.name+'\n'+'我的大小是：'+str(self.size)
        return msg

    def __del__(self):
        pass

    def getName(self):
        return self.name
    def getSize(self):
        return self.size


furniture1=furniture('木床',10)
print(furniture)

home=home()
home.setFurniture(furniture1)
print(home)

furniture2=furniture('钢床',20)
home.lightStatus(1)
home.setFurniture(furniture2)
print(home)