# -*- coding: utf-8 -*-
'''
@File    :   greet_user.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2020/3/13 19:58 
'''
import json

filename = 'username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")
