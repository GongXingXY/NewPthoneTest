# -*- coding: utf-8 -*-
'''
@File    :   electric_car.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2020/3/11 9:31 
'''
# 父类
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

# 编写类时，并非总是从0开始的。如果你要编写的类是另一个现成类的特殊版本，可以使用继承

# 创建子类时，必须在括号内指定父类的名称，方法__init__接受创建父类实例所需的信息


# 将实例用作属性  使用代码模拟实物时，文件越来越长，在这种情况下，可需要将类的一部分作为一个独立的类提取出来。
# 将大型类拆分多个协同工作的小类

# 有关电瓶的都可以详细在这里描述
class Battery():
    '''一次模拟电动汽车电瓶的简单尝试'''

    def __init__(self, battery_size=70):
        '''初始化电瓶的属性'''
        self.battery_szie = battery_size

    def describe_battery(self): 
        '''打印一条描述电瓶容量的消息'''
        print("This car has a " + str(self.battery_szie) + "-kWh battery.")

    def get_range(self):
        '''打印一条消息，指出电瓶的续航里程'''
        if self.battery_szie == 70:
            range = 240
        elif self.battery_szie == 85:
            range = 270
        print(f'This car can go approximately {range} miles on a full charge')

    def upgrade_battery(self):
        if self.battery_szie != 85:
            self.battery_szie = 85
            print('now battery size is 85')



# 子类
class ElectricCar(Car):
    '''电动汽车的独特之处'''

    def __init__(self, make, model, year):
        '''初始化父类的属性，再初始化子类独有的属性'''
        super().__init__(make, model, year) # super是一个特殊函数，帮助python将父类与子类关联起来
        self.battery = Battery()  # 将实例存储在self.battery中


    # 重写父类的方法，假设父类有个关于油箱的方法
    def fill_gas_tank(self):
        '''电动汽车没有油箱'''
        print('This car doesn\'s need a gas tank!')

test = ElectricCar('defa','meodls',2038)

test.battery.describe_battery()
test.battery.upgrade_battery()
test.battery.describe_battery()
test.battery.get_range()



my_tesla = ElectricCar('tesla',' model s', 2016)
print(my_tesla.get_descriptive_name())

# 将实例当用属性
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# 重写父类的方法, 子类定义一个方法，和重写父类方法同名
my_tesla.fill_gas_tank()

