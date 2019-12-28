# -*- coding: utf-8 -*-
'''
@File    :   input.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2019/12/27 12:26 
'''

message = input("tell me something, and I will repeat it back to you:")
print(message)

prompt = "If you tell us who are you, we can personalize the message you are"
prompt += "\nWhat is your first name? : "

name = input(prompt)
print(f'\n Hello, {name} !')

# 用int() 来获取数值的输入 , 用input 来处理 python 会默认为字符串输入

age = input("How old are you?")
age = int(age)
print(age > 18)

# 求模运算符

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f'\n the number {number} is even')
else:
    print(f'\n the number {number} is odd')


