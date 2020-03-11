# -*- coding: utf-8 -*-
'''
@File    :   Practice.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2020/3/11 9:10 
'''
class Restaurant():
    '''一次餐厅的简单尝试'''

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 # 添加就餐人数 默认为0

    def describe_restaurant(self):
        '''显示餐厅名和类型'''
        print(self.restaurant_name + ' ' + self.cuisine_type)

    def open_restaurant(self):
        '''显示餐厅正在营业'''
        print(self.restaurant_name + 'openning')

    def restaurant(self):
        print('There has ' + str(self.number_served) + ' eat')

    def set_number_served(self, served):
        '''设置用餐人数'''
        self.number_served = served

    def increment_number_served(self, add):
        '''设置递增的'''
        self.number_served += add


class IceCreamStand(Restaurant):
    '''冰淇淋独特之处'''

    def __init__(self, restaurant_name, cuisine_type):
        '''初始化父类的属性'''
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['apple','coloe','koro']

    def showflavors(self):

        for x in self.flavors:
            print(x + 'type ice')

# 创建实例
restaurant = Restaurant('YueCai', 'China')
icerestaurant = IceCreamStand('ice','drewb')
icerestaurant.showflavors()

# 打印其中的两个属性
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# 调用其中的两个方法
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 修改用餐人数
restaurant.number_served = 3
restaurant.restaurant()

# 通过方法来修改
restaurant.set_number_served(10)
restaurant.restaurant()

# 通过方法递增
restaurant.increment_number_served(10)
restaurant.restaurant()

