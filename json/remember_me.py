# -*- coding: utf-8 -*-
'''
@File    :   remember_me.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2020/3/13 19:55 
'''
import json

# 如果以前存储了用户名，就加载它,否则，就提示用户输入用户名并存储它
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input('What is your name? ')
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")




