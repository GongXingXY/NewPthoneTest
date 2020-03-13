# -*- coding: utf-8 -*-
'''
@File    :   Practice.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2020/3/13 7:58 
'''

def showfilecount(filename):
    '''读取文件'''
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print(f'Sorry This {filename} dons\'t exites ')
    else:
        print(contents)

filename = ['cats.txt','dogs.txt']
for file in filename:
    showfilecount(file)


print('add number')

while True:
    try:
        firstnumber = int(input('First number: '))
        secondnumbre = int(input('Second number: '))
    except ValueError:
        print('Please enter number')
    else:

        answer = firstnumber + secondnumbre
        print(answer)


