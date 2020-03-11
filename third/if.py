# -*- coding: utf-8 -*-
'''
@File    :   if.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2019/12/27 11:57 
'''
# 条件语句  if

# 检查相等 ==
# 检查不相等 ！=
# 检查大于等于 >=
# 检查小于等于 <=
# 多个条件  and or

# 检查特定值是否不包含在列表中  用关键字 not in
banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
    print(f'{user.title()}, you can post a response if you wish')

number = 23
guess = int(input('Enter an integer:'))

if guess == number:
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
elif guess < number:
    print('No, it is a little higher than that')
else:
    print('No, it is a little lower than that')
if True:
    print('This is true')
print('Done')

#检查特殊元素

requested_toppings = ['mushrooms', 'green peppers','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry, we are out of green peppers right now')
    else:
        print('Adding' + requested_topping + ".")

print("\nFisnished making your pizza")

#列表为空 返回 False

# 省略else代码块  多分支

# 分支结构

confirm = True

while confirm:
    username = input('Enter userName: ')
    password = int(input('Enter passWord: '))
    if username == 'admin' and password == 123456:
        print('身份验证通过')
        break
    elif username == 'admin' and password != 123456:
        print('请检查密码')
    else:
        print('请检查账号')

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))

# Practice1 英制单位英寸与公制单位厘米互换

value = float(input('请输入长度： '))
unit = input('请输入单位： ')
if unit == 'in' or unit == '英寸':
    print('%.1f英寸 = %.1f 厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%.1f厘米 = %.1f英寸' % (value, value / 2.54))
else:
    print('请输入有效单位')

# Practice2 百分制成绩转换为等级制成绩

score = float(input('Enter your score: '))

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')

# Practice3 输入三条边长，如果能构成三角形就计算周长和面积

a = float(input('a = '))
b = float(input('a = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面积：%f' % (area))
else:
    print('不能构成三角形')

# 说明： 上面使用的通过边长计算三角形面积的公式叫做海伦公式。


# 三元运算符
# 语法格式 条件为真的值 if 条件语句 else 条件为假的值

num = input("请输入一个数字: ")

print(num if int(num)<10 else "数字太大了")

