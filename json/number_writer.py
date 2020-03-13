# -*- coding: utf-8 -*-
'''
@File    :   number_writer.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2020/3/13 19:48 
'''
# 存储数据，一种简单的方式是使用模块json来存储数据
# 函数json.dump() 将数字列表存储到文件numbers.json中
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
