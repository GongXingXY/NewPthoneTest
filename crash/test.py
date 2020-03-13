# -*- coding: utf-8 -*-

'''
@File    :   test.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2020/3/13 8:27 
'''
def search(filename):
    '''读取文件'''
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except UnicodeDecodeError:
        print(f'Sorry This {filename} dons\'t exites ')
    else:
        thestring = contents.lower().count('the')
        print(thestring)

story = 'a.txt'

search(story)
