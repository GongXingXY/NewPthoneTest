# -*- coding: utf-8 -*-
'''
@File    :   dog.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2020/3/11 7:57 
'''
'''
Python 中，“一切皆对象”。类也称为“类对象”，类的实例也称为“实例对象”。
定义类的语法格式如下：
class 类名：
类体
要点如下：
1. 类名必须符合“标识符”的规则；一般规定，首字母大写，多个单词使用“驼峰原则”。
2. 类体中我们可以定义属性和方法。
3. 属性用来描述数据，方法(即函数)用来描述这些数据相关的操作。
'''
# __init__ 方法会在类的对象被实例化（Instantiated）时立即运行。
# 这一方法可以对任何你想进行操作的目标对象进行初始化（Initialization）操作。
# 这里你要注意在 init 前后加上的双下划线。

class Dog():  # 首字母大写指的是类
    '''模拟小狗的简单尝试'''

    def __init__(self, name, age):
        '''初始化属性name 和 age'''
        self.name = name
        self.age = age

    def sit(self):
        '''模拟小狗被命令时蹲下'''
        print(self.name.title() + "is now sitting")

    def roll_over(self):
        '''模拟小狗被命令时打滚'''
        print(self.name.title() + "rolled over!")

# 类中的函数称为方法
# __init__ 是一种特殊的方法，当前类每次创建新的实例都会自动运行它，下划线是为了名称冲突，是指定的
# __init__ 定义成了包含三个形参， self name age 形参 self 不可少，必须位于其他形参前面

# 根据类 创建实例
my_dog = Dog('willie', 6)
your_dog = Dog('black', 8) #创建多个实例

# 访问属性
print(f'My dog\'s name is {my_dog.name.title()} .')
print(f'My dog is {my_dog.age} years old .')

#访问方法
my_dog.sit()
my_dog.roll_over()

