# -*- coding: utf-8 -*-
'''
@File    :   pizza.py.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2020/2/16 11:41 
'''
def make_pizza(size, *toppings):
    '''概述要制作的比萨'''
    print(f'\nMaking a {size} -inch pizza with the following toppings:')
    for topping in toppings:
        print("-" + topping)