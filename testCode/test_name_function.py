# -*- coding: utf-8 -*-
'''
@File    :   test_name_function.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2020/3/13 21:21 
'''
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):  # 这个测试类 继承unittest.TestCase
    '''测试name_function.py'''

    def test_first_last_name(self):
        '''能够正确地处理像Jains Joplin 这样的名字吗？'''
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')  # unittest 最有用的功能之一 断言方法

unittest.main()
