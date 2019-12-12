# -*- coding: utf-8 -*-
'''
@File    :   var.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2019/12/11 10:03 
'''
# 变量  Variable

# 所谓物理行（Physical Line）是你在编写程序时 你所看到 的内容。
# 所谓逻辑行（Logical Line）是 Python 所看到 的单个语句。Python 会假定每一 物理行 会对应一个 逻辑行。


print('Hello World')
#   变量的命名与规则
'''
只能包含字母、数字和下划线，不能包含空格
不要将关键字和函数名用作变量
简短又具有描述性。例如 name 比 n 好 student_name 比 s_n 好
慎用小写字母l 和 大写字母 O 因为它们可能会被看成是 1 和 0
'''
'''
对象：
Python中一切皆对象。每个对象由：标识（Identity) 、类型（type)、值（value)组成

1. 标识用于唯一标识对象，通常对应于对象在计算机内存中的地址。使用内置函数 id(obj) 可返回对象 obj 的标识。

2. 类型用于表示对象存储的“数据”的类型。类型可以限制对象的取值范围以及可执行的 操作。可以使用 type(obj)获得对象的所属类型。

3. 值表示对象所存储的数据的信息。使用 print(obj)可以直接打印出值。'''

a = 321
b = 123

print(id(a))  # 获取标识，用内置函数id(obj)可返回对象obj的标识
print(type(a)) # 类型 用于表示对象存储的“数据"的类型 type(obj)
print(a)  # 值表示对象所存储的数据的信息

# 基本变量运算
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)


# type() 检查变量的类型

a = 100
b = 12.345
c = 1 + 5j
d = 'helloworld'
e = True
def sayhi():
    print('hi')
class Test():
    def hello(self):
        print('hello')

fun = sayhi
cla = Test()

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(fun))
print(type(cla))

# Python内置函数对变量类型进行转换
'''

int() 将一个数值或者字符串转换成整数，可以指定进制
1. 浮点数直接舍去小数部分。如：int(9.9)结果是：9
2. 布尔值 True 转为 1，False 转为 0。 如：int(True)结果是 1
3. 字符串符合整数格式（浮点数格式不行）则直接转成对应整数，否则报错

float() 将一个字符串转换成浮点数
1. 类似于 int()，我们也可以使用 float()将其他类型转化成浮点数。
2. 整数和浮点数混合运算时，表达式结果自动转型成浮点数。比如：2+8.0 的结果是 10.0
3. round(value)可以返回四舍五入的值
注：但不会改变原有值，而是产生新的值

str() 将指定对象转换成字符串形式，可以指定编码


chr() 将整数转换成该编码对应的字符串(一个字符)
ord() 将字符串（一个字符）转换成对应的编码（整数）

'''
test = 10
teststr = str(test)
print(teststr + 'e')
print(type(teststr))

a = 5; b = 8
# python 中交换两个变量的最快方法是：
a, b = b, a

print(a, b)
# a = 8  b = 5

'''关于常量：Python中没有常量的，没有语法规则限制改变一个常量的值

常量的命名规则：全大写 '''

PI = 3.14
print(PI)


