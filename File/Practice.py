# -*- coding: utf-8 -*-
'''
@File    :   Practice.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2020/3/12 20:43 
'''

print('Please enter your name')

username = input('Enter: ')

filename = 'test/guest.txt'

with open(filename,'w') as file_object:
    file_object.write(username + '\n')

ok = True
while ok:
    hello = input('Enter your name: ')
    if hello == 'q':
        break
    else:
        with open(filename,'a') as file_object:
            file_object.write(f'hello, {hello}\n')