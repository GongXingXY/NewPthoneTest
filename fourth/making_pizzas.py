# -*- coding: utf-8 -*-
'''
@File    :   making_pizzas.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2020/2/16 11:43 
'''
from pizza import make_pizza

# 导入特定的函数

# from module_name import function_name

# from module_name import function_name1, function_name2


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms','green peppers', 'extra cheese')

# 使用as 来给函数指定别名
# from module_name import function_name as fn

from pizza import make_pizza as mp
mp(1,'mp')

#使用as 来给模块指定别名
# import module_name as mn
import pizza as p

p.make_pizza(2,'p')

# 导入模块中的所有函数
#from module_name import *