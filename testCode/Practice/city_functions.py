# -*- coding: utf-8 -*-
'''
@File    :   city_functions.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2020/3/14 8:27 
'''
def citycountry(city, country, population = ''):
    '''接受城市名和国家名 并返回'''
    if population:
        full = city + ',' + country +'-population=' + str(population)
    else:
        full = city + ',' + country

    return full.title()
