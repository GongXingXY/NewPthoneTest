# -*- coding: utf-8 -*-
'''
@File    :   write_message.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2020/3/12 20:50 
'''
filename = 'test\programming.txt'

# open 传入两个 参数 ，第一个是文件名，第二个是write 写入权限 r 读取
#写入
with open(filename, 'w') as file_object:
    file_object.write('I love programming.\n')
    file_object.write('I love creating new games\n')

# 附加内容，也不是添加内容的话 加 a

with open(filename, 'a') as file_object:
    file_object.write('I also love finding meaning in large datasets.\n')
    file_object.write('I love creating apps that can run in a browser.\n')


