# -*- coding: utf-8 -*-
'''
@File    :   favorite_languages.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2020/3/11 18:44 
'''

from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + '.')