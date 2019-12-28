# -*- coding: utf-8 -*-
'''
@File    :   thirdPractice.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2019/12/28 11:49 
'''
car = input("what is your asked car? ")

print(f'Let me see if I can find you a {car}')

dinnernumber = input("your guys is number what?")
dinnernumber = int(dinnernumber)
if dinnernumber > 8:
    print("Sorry, on empty there")
else:
    print("wellcom")

number = input("Enter a number, ten or no ten")
number = int(number)
if number % 10 == 0:
    print(f'yeah this number {number} is ten')
else:
    print(f'no this number {number} no ten')

# while

promt = '\n Enter you pizza:'
promt += '\n (Enter "quit" end the progam'
active = True
while active:
    message = input(promt)
    if message == 'quit':
        active = False
    else:
        print(message)