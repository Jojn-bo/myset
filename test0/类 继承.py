class people:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __del__(self):
        pass
    def weight(self):
        print('My weight is not defind....')
    def high(self):
        print('My high is not defind...')
    def sleep(self):
        print('People is sleep.....')

class Man(people):
    def sleep(self):
        people.sleep(self)
        print('Man is sleep...')


m1 = Man('BO',11)
m1.sleep()