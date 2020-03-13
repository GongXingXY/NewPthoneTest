# -*- coding: utf-8 -*-
'''
@File    :   alice.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2020/3/13 7:43 
'''
# 处理FileNot FoundError 异常 找不到文件

filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print(f'Sorry, the file {filename} does not exist')
