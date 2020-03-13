# -*- coding: utf-8 -*-
'''
@File    :   file_reader.py.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2020/3/12 20:13 
'''
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# open函数  打开文件  open('filename') 文件所在目录


with open('test/a.txt') as file_object: # 绝对路径 windows系统用绝对目录 \反斜杠

    print(file_object.read())

# 逐行读取

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))


# 使用文件内容
