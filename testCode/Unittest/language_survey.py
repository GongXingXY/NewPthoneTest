# -*- coding: utf-8 -*-
'''
@File    :   language_survey.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2020/3/14 9:10 
'''

from survey import AnonymousSurver

# 定义一个问题，并创建一个表示 调查AnonymousSurvey对象

question = "What language did you first learn to speak? "

my_survey = AnonymousSurver(question)

# 显示答案 并存储答案
my_survey.show_question()
print('Enter q at any tim to quit.\n')
while True:
    response = input('Language: ')
    if response == 'q':
        break
    my_survey.store_responses(response)

# 显示调查结果
print("\nThank you to everyone who participated in the survey! ")
my_survey.show_results()
