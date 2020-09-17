# -*- coding: utf-8 -*-
'''
@File    :   test.cities.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2020/3/14 8:29 
'''
import unittest
from city_functions import citycountry

class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        '''可以返回这样的城市国家格式吗'''

        formatted_full = citycountry('santiago', 'chile')
        self.assertEqual(formatted_full,'Santiago,Chile')

    def test_city_country_population(self):
        '''可以返回'santiago chile population = 500000这样的值'''
        formatted_full = citycountry('santiago', 'chile', '500000')
        self.assertEqual(formatted_full, 'Santiago,Chile-Population=500000')


unittest.main()

