# -*- coding: utf-8 -*-
'''
@File    :   Practice.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2019/12/11 10:40 
'''
# Practice & Classwork

name = 'Eric'
print('Hello ' + name + ', would you like to lean some Python')
print(name.lower())
print(name.upper())
print(name.title())

import math
import random
#1、用print函数打印多个值
print('#1')
print('a','1','c')

print('#2')
#2、用print函数不换行打印
print('1',end='')
print('不换行')
#3、导入模块的方式有哪些
# 1）from 模块 import 函数
# from keyword import kwlist,iskeyword
# print(kwlist)
# print(iword('True'))skey

# 2）import 模块
# import keyword
# print('1111')=
# print(keyword.kwlist)

# 3）from 模块 import *
# from keyword import *
# print(kwlist)
# # print(iword('True'))skey

# 4、python有哪六种数据类型？不可变数据类型有哪些？可变数据类型有哪些？
print('#4')
print('number')  # 数字类型  不可变类型
print('string')  # 字符串类型  不可变类型
print('list')    # 列表   可变类型
print('tuple')   # 元组   不可变类型
print('dict')    # 字典    可变类型
print('set')     # 集合    可变类型


# 5、python3中可以支持哪些数值类型？
#  int 整形，不带小数点
# float 浮点数，带小数点
#  bool 布尔,  0 1 真假
# complex  由实数、虚数组成，a+bj或者complex(a,b)

# 6、判断变量类型有哪些方式，分别可以用哪些函数？
# 查看变量类型 type
print('#6')
print(type(1)) # int
# isinstance(对象,类型)如果对象与类型一致返回True，否则返回False


'''7、分别对49.698作如下打印
	1）四舍五入，保留两位小数
	2）向上入取整
	3）向下舍取整
	4）计算8除以5返回整型
	5）求4的2次幂
	6）返回一个（1,100）随机整数
	'''
num = 49.698
print('#7')
print(round(num,2))
print(math.ceil(num))
print(math.floor(num))
print(8//5)
print(4**2)
print(random.randint(1,100))

# 8、依次对变量a,b,c赋值为1,2,3
a, b, c = 1, 2, 3
print('#8')
print(a, b, c)

# 9、截取某字符串中从2索引位置到最后的字符子串
str = 'abcdefge'
print('#9')
print(str[1:])

'''10、对字符串“testcode”做如下处理：

	1）翻转字符串

	2）首字母大写

	3）查找是否包含code子串，并返回索引值

	4）判断字符串的长度

	5）从头部截取4个长度字符串

	6）把code替换为123

	7）把“test code”字符串中的两个单词转换为列表中的元素，并打印处理

	8）把['test','code']把list变量中的元素连接起来
'''
testcode = 'testcode'
print('#10')
print(testcode[::-1])
print(testcode.title())
print(testcode.find('code',0, len(testcode)))
print(len(testcode))
print(testcode[0:4])
test = "test code"
print(test.split(' '))
testlist = ['test','code']
print(''.join(testlist))


# 11、如何打印出字符串“test\ncode”
print('#11')
print('test\\ncode')


# 12、如何创建一个空元组
empty = []
print('#12')
print(empty)
# 13、创建一个只包含元素1的元组，并打印出该变量的类型
print('#13')
onetuple = (1,)
print(onetuple[0])

# 14、元组中元素可以修改？如何更新元组中的元素？
# 元组的元素不能修改
'''
元组是不可变类型，不能更新或者改变元组的元素。
通过现有字符串的片段在构造一个新的字符串的方式来等同于更新元组操作。
'''
#通过索引更新
print('#14')
tuple_1 = (1,2,34,5)
tuple_1=(tuple_1[0],tuple_1[2],tuple_1[3])
print(tuple_1)
#通过切片更新
tuple_1=(tuple_1[0:2])
print (tuple_1)




'''15、对元组（1,2,3,4,5)做如下操作：

	1）取倒数第二个元素

	2）截取前三个元组元素

	3）依次打印出元组中所有元素
'''
tuplea = (1, 2, 3, 4, 5)
print('#15')
print(tuplea[3])
print(tuplea[0:3])
print(tuplea)

# 16、把元组(1,2,3,4,5,6)元素格式化成字符串
print('#16')
tupleb = (1, 2, 3, 4, 5, 6)
tupstr = tupleb.__str__()
print(tupstr)
print(type(tupstr))

# 17 格式化输出
# 1
print('%d + %d = %d' % (a, b, a + b))
# 2
print('{} + {} = {}'.format(a, b, a+b))
# 3 format的语法糖
num1, num2 = 5, 10
print(f'{num1} * {num2} = {num1 * num2}')



