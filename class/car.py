# -*- coding: utf-8 -*-
'''
@File    :   car.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2020/3/11 8:42 
'''
class Car():
    '''一次模拟汽车的简单尝试'''

    def __init__(self, make, model, year):
        '''初始化描述汽车的属性'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # 给属性指定默认值

    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        '''打印一条指出汽车里程的消息'''
        print('This car has ' + str(self.odometer_reading) + " miles on it.")

    # 写一个更新属性的方法来修改，扩展，加一些逻辑，禁止任何人把里程表读数往回调
    def update_odometer(self, mileage):
        '''将里程表读数设置为指定的值，禁止往回调，判断大小'''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage  # mileage 的值存储到odometer_reading
        else:
            print("You can't roll back an odometer! ")

    # 通过方法对属性的值进行递增
    def increment_odometer(self, miles):
        '''将里程表读数增加指定的值'''
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print('You can\'roll back an odometer! ')



# 修改属性的值
# 可以通过三种方法来 1 直接通过实例进行修改 2通过方法来设置 3 通过方法来进行递增（增加特定的值）

my_newcar = Car('audi', 'a4', 2016)
print(my_newcar.get_descriptive_name())
my_newcar.read_odometer()

# 1直接通过实例来修改访问
my_newcar.odometer_reading = 23
my_newcar.read_odometer()

# 2通过方法修改属性的值
my_newcar.update_odometer(33)
my_newcar.read_odometer()

# 3通过方法对属性的值进行递增
you_oldcar = Car('subaru','outback', 2013)
print(you_oldcar.get_descriptive_name())

you_oldcar.update_odometer(23500)
you_oldcar.read_odometer()

you_oldcar.increment_odometer(100)
you_oldcar.read_odometer()