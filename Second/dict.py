# -*- coding: utf-8 -*-
'''
@File    :   dict.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2019/12/17 7:54 
'''

'''字典就像一本地址簿，如果你知道了他或她的姓名，你就可以在这里找到其地址或是能够联系上对方的更多详细信息，换言之，我们将键值（Keys）（即姓名）与值（Values）（即地址等详细信息）联立到一起。在这里要注意到键值必须是唯一的，正如在现实中面对两个完全同名的人你没办法找出有关他们的正确信息。
另外要注意的是你只能使用不可变的对象（如字符串）作为字典的键值，但是你可以使用可变或不可变的对象作为字典中的值。基本上这段话也可以翻译为你只能使用简单对象作为键值。
在字典中，你可以通过使用符号构成 d = {key : value1 , key2 : value2} 这样的形式，来成对地指定键值与值。在这里要注意到成对的键值与值之间使用冒号分隔，而每一对键值与值则使用逗号进行区分，它们全都由一对花括号括起。'''
# 字典是属于 dict 类下的实例或对象。

# “ab”是地址（Address）簿（Book）的缩写

ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang',
    'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is", ab['Swaroop'])

# 删除一对键值-值配对
del ab['Spammer']

print('\n There are {} contacts in thee address-book\n'.format(len(ab)))

# item方法访问键值与值的信息
for name, address in ab.items():
    print('{}Contact {}'.format(name, address))
print('字典遍历方法')
# 对字典进行遍历(遍历的其实是键再通过键取的值)
for key in ab:
    print(f'{key} Contact  {ab[key]}')

# 添加一对键值-值配对
ab['Guido'] = 'guido@python.org'

# 判定值是否存在
if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])

'''
字典是另一种可变容器模型,类似于我们生活中使用的字典,它可以存储
任意类型对象,与列表,集合不同的是,字典的每个元素都是由一个键
和一个值组成的'键值对',健和值通过冒号分开.下面的代码演示了如何定义和
使用字典

'''

scores = {'骆昊':95, '沙发椅':78, '李白 ':82}
# 通过键可以获取字典中对应的值
print(scores['骆昊'])
print(scores['沙发椅'])
#　对字典进行遍历(遍历的其实是键再通过键取的值)
for elem in scores:
    print('%s\t --> \t%d' % (elem, scores[elem]))

# 更新字典中的元素
scores['少数人'] = 65
scores['诸葛王良'] = 71
scores.update(冷面=67, 方 = 85)
print(scores)

if '武则天' in scores:
    print(scores['武则天'])
print(scores.get('武则天'))
# get方法 也是通过键获取对应的值,但是可以设置默认值
print(scores.get('武则天', 60))
# 删除字典中的元素
print(scores.popitem())
print(scores.popitem())
print(scores.pop('骆昊', 100))
# 清空字典
scores.clear()
print(scores)

alien_0 = {'color': 'green', 'points':5}
new_points = alien_0['points']
# new_points = alien_0.get('points') # 也可以用get方法获取键的值
print(f'You just earned {new_points} points!')
# 添加元素
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
for key in alien_0:
    print(key)
for key in alien_0:
    print(alien_0[key])
for elem in alien_0:
    print(f'{elem}:{alien_0[elem]}')
# 修改元素
alien_0['color'] = 'yellow'
print(alien_0)

# 删除元素
del alien_0['points']
print(alien_0)

# 还有一种格式， 由类似对象组成的字典
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'java'
}
print(f"sarah\'s favorite_languages is {favorite_languages['sarah'].title()}")
for elem in favorite_languages:
    print(f"{elem}\'s favorite_languages is {favorite_languages[elem].title()}")

# 遍历元组
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
# 用元组的items()来遍历
print('items来遍历')
for x, y in user_0.items():
    print('\nkey: ' + x)
    print('\nvalue: ' + y)
# 用键 和键值
print('用键和键值')
for elem in user_0:
    print(f'\nkey: {elem}')
    print(f'\nvalue: {user_0[elem]}')




# 遍历字典中所有的键
# 用keys方法
print('用keys方法')
for name in favorite_languages.keys():
    print(name.title())
print('用键方法')
for key in favorite_languages:
    print(key.title())

# 按顺序遍历字典中的所有键 用sored()

for name in sorted(favorite_languages.keys()):
    print(name.title() + ",thank you for taking the poll.")

# 字典列表  把字典放到列表里面

alien_0 = {'color': 'green', 'point': 5}
alien_1 = {'color': 'yellow', 'point': 10}
alien_2 = {'color': 'red', 'pint': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

#随机生成30个机器人

aliens30 = []

for alien_number in range(30):
    new_aliens = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens30.append(new_aliens)

for alien in aliens30[:5]:
    print(alien)
print('...')

print(f'Total number of aliens: {len(aliens30)}')

# 字典存储列表

pizza = {
    'crust': 'tick',
    'toppings': ['mushrooms', 'extra cheese']
}

print(f"You ordered a {pizza['crust']}-crust pizza with the floolwing toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
