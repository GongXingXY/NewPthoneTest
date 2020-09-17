# -*- coding: utf-8 -*-
'''
@File    :   survey.py
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2020/3/13 21:21 
'''
'''
6个常用的断言方法
assertEqual(a, b)  比较 a == b
assertNotEqual(a, b) 比较 a!= b
assertTrue(x)  核实 x 为True
assertFalse(x)  核实 x 为False
assertIn(Item,list) 核实 item在list中
assertNotIn(item,list) 核实item 不在list中
'''
# 一个要测试的类
class AnonymousSurver():
    '''收集匿名调查问卷的答案'''
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        '''显示调查问卷'''
        print(self.question)

    def store_responses(self, new_response):
        '''存储单份调查答卷'''
        self.responses.append(new_response)

    def show_results(self):
        '''显示收集到的所有答卷'''
        print("Survey results: ")
        for response in self.responses:
            print('-' + response)




