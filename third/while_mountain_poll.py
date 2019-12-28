# -*- coding: utf-8 -*-
'''
@File    :   while_mountain_poll.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2019/12/28 12:48 
'''

# 使用用户输入来填充字典

responses = {}

# 设置一个标志，指出调查是否继续
polling_active = True
while polling_active:
    #提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain whould you lick to climb someday? ")
    responses[name] = response # 将答卷存储在字典中

    # 看看是否还有人要参与调查
    repeat = input('Would you like to let another perso respond? (yes/no)')
    if repeat == 'no':
        polling_active = False

print('\n --- Poll Results ---')
for elem in responses:
    print(f'{elem} would like to climb {responses[elem]}.')

