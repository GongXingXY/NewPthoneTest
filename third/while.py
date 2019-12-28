# -*- coding: utf-8 -*-
'''
@File    :   while.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2019/12/28 11:56 
'''
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = '\nTell me something, and I will reepeat it back you'
prompt += '\nEnter "quit" to end the program.'

'''
message = ''
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)
'''
# 使用标志
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# break
prompt2 = '\nPlease enter the name of a city you have visited: '
prompt2 += '\n(Enter "quit" when you are finished.'

while True:
    city = input(prompt2)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()} !")

# continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)



