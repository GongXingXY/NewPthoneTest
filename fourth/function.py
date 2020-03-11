# -*- coding: utf-8 -*-
'''
@File    :   function.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2019/12/30 8:53 
'''
'''
定义函数
在Python中可以使用def关键字来定义函数，和变量一样每个函数也有一个响亮的名字，
而且命名规则跟变量的命名规则是一致的。在函数名后面的圆括号中可以放置传递给函数的参数，
这一点和数学上的函数非常相似，程序中函数的参数就相当于是数学上说的函数的自变量，
而函数执行完成后我们可以通过return关键字来返回一个值，这相当于数学上说的函数的因变量。

1. 一个程序由一个个任务组成；函数就是代表一个任务或者一个功能。
2. 函数是代码复用的通用机制。

Python 中函数分为如下几类：
1. 内置函数
我们前面使用的 str()、list()、len()等这些都是内置函数，我们可以拿来直接使用。
2. 标准库函数
我们可以通过 import 语句导入库，然后使用其中定义的函数
3. 第三方库函数
Python 社区也提供了很多高质量的库。下载安装这些库后，也是通过 import 语句导
入，然后可以使用这些第三方库的函数
4. 用户自定义函数
用户自己定义的函数，显然也是开发中适应用户自身需求定义的函数。今天我们学习的
就是如何自定义函数。

'''

def printMax(a, b):
    '''判断两个数的大小'''
    if a > b:
        print(a, '较大值')
    else:
        print(b, '较大值')

printMax(10, 20)
# 向函数传递参数
def greet_user(username):  # username 是形参
    print(f'Hello {username.title()} !')

greet_user('jesse')  # 实际调用了 是 实参

# 位置实参

def describe_pet(animal_type, pet_name):

    '''显示宠物信息''' # 文档字符串（函数的注释）
    print(f'\nI have a {animal_type}.')
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
# 调用函数多次
describe_pet('dog', 'willie')

# 注意参数前后顺序

# 关键字实参
describe_pet(animal_type='cat', pet_name='beby')

# 默认值
def describe_pet2(pet_name, animal_type = 'dog'):

    '''显示宠物信息'''
    print(f'\nI have a {animal_type}.')
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet2('test')
describe_pet2('test','ee')

# 返回值

def get_formatted_name(first_name, last_name):
    '''显示整洁的名字'''
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

def build_persion(firstname, lastname, age=''):
    person = {'first': firstname, 'last':lastname}
    if age:
        person['age'] = age
    return person
test = build_persion('drew','better', age='33')
print(test)

# 结合使用函数和while循环

while True:
    print('\nPlease tell me your name:')
    print('enter "q" at any time to quit')
    f_name = input('First name:')
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f'Hello, {formatted_name}! ')

# 传递列表

def greet_users(names):
    '''向列表中的每位用户都发出简单的问候'''
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hann', 'app', 'margot']

greet_users(usernames)


# 在函数中修改列表

'''需要打印的设计存储在一个列表中，打印后移到另一个列表中'''

def print_models(unprinted_designs, comleted_designs):
    '''模拟打印每个设计，直到未打印的设计为止
    打印每个设计后，都将其移到列表completed_designs中
    '''
    while unprinted_designs:
        current_designs = unprinted_designs.pop()
        # 模拟根据设计制作3 D 打印模型的过程
        print(f'Printing model: {current_designs}')
        comleted_designs.append(current_designs.title())

def show_completed_models(completed_models):
    '''显示打印好的所有模型'''
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot penndant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)

# 禁止函数修改列表

# 可以在调用函数的时候，传入列表的副本，这样就不会影响修改到原来的列表
# 通过切片表示法[:]创建列表的副本
'''function_name(list_name[:])'''

#传递任意数量的实参
''' 有时候，你不知道函数需要接受多少个实参，'''

def make_pizza(size, *toppings): # 形参名*toppings中的星号让python创建一个名为toppings的空元组
    '''打印顾客点的所有配料'''
    print(f'\nMaking a {size} -inch pizza with the following topings:')
    for topping in toppings:
        print(f'-{topping}')

make_pizza(16,'peeperoni')
make_pizza(28,'mushrooms', 'green peppers', 'extra cheese')

# 不管函数收到的实参多少个，这个方法都管用。

# 结合使用位置实参和任意数量实参

# 使用任意数量的关键字实参 **

def build_profile(first, last, **user_info):
    '''创建一个字典，其中包含我们知道的有关用户的一切 '''
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert','einstein',
                             location = 'princeton',
                             filed = 'physics')
print(user_profile)