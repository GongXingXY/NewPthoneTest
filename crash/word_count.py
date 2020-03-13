# -*- coding: utf-8 -*-
'''
@File    :   word_count.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2020/3/13 7:48 
'''
# 写个计算一个文件大致包含多少个单词
def count_words(filename):
    '''计算一个文件大致包含多少个单词'''
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
       '''print(f'Sorry, the file {filename} does not exist')'''
       pass
    else:
        '''计算文件大致包含多少个单词'''
        words = contents.split()
        num_words = len(words)
        print(f'The file {filename} has about {num_words} words')

filename = ['a.txt','b.txt','c.txt']
for file in filename:
    count_words(file)

# 失败时不发出信号 用 pass