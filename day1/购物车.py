import os
import time
#定义一个商品表
product_list = [
    ('iphone',5800),
    ('mac pro',9800),
    ('Bike',800),
    ('Watch',10600),
    ('Coffee',30),
    ('Alex Python',120)
]
#定义一个购物车列表
shopping_list = []

salary = input ('input your salary:')
if salary.isdigit():#判断是否是数字
    salary = int(salary)#是数字就转换成int
    while True:
        for index,item in enumerate(product_list):#循环打印出商品列表
            print(index+1,item)
        user_choice = input('选择要买啥？》》》')
        if user_choice.isdigit():#判断是否是数字
            user_choice = int(user_choice)
            if user_choice <= len(product_list) and user_choice >=0:#判断是否超过商品表的最大和最小个数
                p_item = product_list[user_choice-1]#把商品列表中的该列商品使用一个变量存储
                if p_item[1] <= salary:#判断商品的价格是否小于工资
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print('Added \033[31;1m {0} \033[0m into shopping cart,your current balance is \033[31;1m {1} \033[0m'.format(p_item,salary))
                else:
                    print('Not enough salary!')
                    print('\n'*80)#伪清屏
        elif user_choice == 'q':
            print('exit......')
            print('You buy:')
            for temp in shopping_list:
                print(temp[0]+',',end='')
            print('Welcome Again!')
            time.sleep(2)
            exit()
        else:
            print('invalid option')
            time.sleep(2)
            print('\n' * 80)
else:
    print('you input is no digit!')