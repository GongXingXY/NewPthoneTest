# -*- coding: utf-8 -*-
'''
@File    :   employee.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2020/3/14 10:04 
'''
class Employee():
    '''编辑一个雇员的类，包含名，姓，年薪'''

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def give_raise(self, add = 500):
        if add == 500:
            self.salary += 500
        else:
            self.salary += add
        return self.salary



