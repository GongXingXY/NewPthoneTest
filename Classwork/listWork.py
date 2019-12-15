# -*- coding: utf-8 -*-
'''
@File    :   listWork.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2019/12/15 19:03 
'''

# 列表练习 3.1
name = ['xing','zhong','hang','jing']
print(name[0])
print(name[1])
print(name[2])
print(name[3])
for x in name:
    print(f'{x} hello there...')

# 列表 3.2

dinner = ['Yangyuhuan', 'Libai', 'Yubo']
print(dinner[1] + '喝醉了不能来了')
dinner[1] = 'Dufu'
for x in dinner:
    print(f'hello {x}, please join my dinner')
print('I got big one')
dinner.insert(0, 'Xixi')
dinner.insert(2,'YeFei')
dinner.append('Zhuyunwen')
for x in dinner:
    print(f'hello {x}, please join big one ')
print('Sorry,this one I just two guy')

sorry1 = dinner.pop()
print(sorry1 + " I'm sorry ")
sorry2 = dinner.pop()
print(sorry2 + " I'm sorry ")
sorry3 = dinner.pop()
print(sorry3 + " I'm sorry ")
sorry4 = dinner.pop()
print(sorry4 + " I'm sorry ")

for x in dinner:
    print(f'{x} guys join dinner')
del dinner[0]
del dinner[0]
print(dinner)

# 列表 3.4
two = [value for value in range(1, 21)]
print(two)

million = [value for value in range(1, 1000001)]
'''for value in million:
    print(value)
'''
print(min(million))
print(max(million))
print(sum(million))

odd = [value for value in range(1, 21, 2)]
print(odd)

list3 = []
for value in range(3,31):
    if value % 3 == 0:
        list3.append(value)
print(list3)

sqeury = [value ** 3 for value in range(1, 11)]
print(sqeury)

