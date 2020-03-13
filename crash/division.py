# -*- coding: utf-8 -*-
'''
@File    :   division.py
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2020/3/13 7:31 
'''
# 当你认为可能发生了错误时，可编写一个try-except 代码块来处理异常
try:
    print(5/0)
except ZeroDivisionError:  # 处理Zero情况
    print('You can\'t divide by zero')

print('Give me two numbers, and I \'ll divide them.')
print('Enter Q to quit')

while True:
    first_number = input('\nFirst number: ')
    if first_number == 'q':
        break
    second_number = input('Second_number: ')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('You can\'t divide by 0')
    else:
        print(answer)

