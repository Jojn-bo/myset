class Dog:
    def __init__(self,weight,color,age):
        self.weight = weight
        self.color = color
        self.age = age

    def run(self):
        print('汪...')

    def eat(self,food,nums):
        print('正在吃{}'.format(food))
        # self.weight+=nums
        print('体重增加{}斤，现在体重{weight}斤'.format(nums,weight=self.weight+nums))

    def infomation(self):
        print('现在的信息是:')
        print('1、体重：{}'.format(self.weight))
        print('2、颜色：{}'.format(self.color))
        print('3、年龄：{}'.format(self.age))

dahuang=Dog(5,'黄色',10)
dahuang.eat('肉',15)
dahuang.infomation()