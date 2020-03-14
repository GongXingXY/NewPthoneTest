# -*- coding: utf-8 -*-
'''
@File    :   test_employee.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2020/3/14 10:09 
'''
import unittest
from employee import Employee

class SalaryTestCase(unittest.TestCase):

    def setUp(self):
        '''创建年薪'''
        self.auto_employee = Employee('Android','Ios', 1000)

    def test_give_default_raise(self):
        self.assertEqual(self.auto_employee.give_raise(), 1500)


    def test_give_custom_raise(self):
        self.assertEqual(self.auto_employee.give_raise(600),1600)




"""
    def test_give_default_raise(self):
        '''测试默认年薪'''
        my_employee = Employee('Drew', 'B', 500)
        salary_raise = my_employee.give_raise()
        self.assertEqual(salary_raise, 1000)

    def test_give_custom_raise(self):
        '''测试接受其它值年薪'''
        you_employee = Employee('DrewC', 'C',600)
        salary_raise = you_employee.give_raise(500)
        self.assertEqual(salary_raise,1100)
"""
if __name__ == 'main':
    unittest.main()
