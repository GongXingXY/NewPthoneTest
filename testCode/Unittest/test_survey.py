# -*- coding: utf-8 -*-
'''
@File    :   test_survey.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2020/3/14 9:23 
'''

import unittest
from survey import AnonymousSurver

class TestAnonymousSurvey(unittest.TestCase):
    '''针对AnonymouSurey 类的测试'''


    def setUp(self):
        '''方法setUP().
          创建一个调查对象和一组答案，共使用的测试使用
          '''
        question = 'What language did you first learn to speak? '
        self.my_surver = AnonymousSurver(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        '''测试单个答案会被妥善地存储'''
        self.my_surver.store_responses(self.responses[0])
        self.assertIn(self.responses[0], self.my_surver.responses)

    def test_store_three_response(self):
        '''测试三个答案会被妥善地存储'''
        for response in self.responses:
            self.my_surver.store_responses(response)
        for response in self.responses:
            self.assertIn(response, self.my_surver.responses)

"""
    def test_store_single_response(self):
        '''测试单个答案会被妥善地存储'''
        question = 'What language did you first learn to speak? '
        my_survey = AnonymousSurver(question)
        my_survey.store_responses('English')

        self.assertIn('English', my_survey.responses)  # 断言 English包含在my....中

    def test_store_tree_responses(self):
        '''测试三个答案都会被妥善保存'''
        question = "What language did you first learn to speak? "
        my_survey = AnonymousSurver(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_responses(response)

        for response in responses:
            self.assertIn(response, responses)
"""

if __name__ == 'main':  #当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行。
    unittest.main()


