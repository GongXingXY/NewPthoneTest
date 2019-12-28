# -*- coding: utf-8 -*-
'''
@File    :   while_confirmed_users.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2019/12/28 12:27 
'''
# while 中 处理列表和字典
unconfirmed_users = ['alice', 'brian', 'candace'] # 创建待验证列表
confirmed_users = []  # 创建空列表 存储已验证列表

while unconfirmed_users: # 列表有值为真，真到列表为空 为假
    current_user = unconfirmed_users.pop() # 末尾删除未验证用户
    print(f'Verifying users: {current_user.title()}')
    confirmed_users.append(current_user) # 添加到已验证列表

print("\n The following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# 删除包含特定值的所有列表元素

pets = ['dog', 'cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)