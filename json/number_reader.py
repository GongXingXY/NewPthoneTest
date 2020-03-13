# -*- coding: utf-8 -*-
'''
@File    :   number_reader.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2020/3/13 19:52 
'''
# json.load() 将列表读取到内存中
import json

filename = 'numbers.json'

with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)
