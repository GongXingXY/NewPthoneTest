# -*- coding: utf-8 -*-
'''
@File    :   number.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2019/12/11 10:47 
'''
# 数字 Number

import math
import random

'''
在编程中，经常使用数字来记录游戏得分，表示可视化数据、存储Web应用信息等
'''
print(2 ** 3) # 8  乘方

var1=4
var2=1
var3='1'
print(type(var1))
print(type(var3))
print(isinstance(var3,int))
print(type(var2))

var4=complex(1,1.1)
print(var4,var4.real,var4.imag,var4.conjugate())

# 数字类型进行运算（+ - * / //  ** ）

print(var1+var2,var1*var2)
print(var1/var2)  # /返回的是float
# 返回整型
print(type(var1//var2))

print(4//2.0)
print(4.0//2)
print(8//3)  #向下取整数
print(8/3)

print(type(int(2.0)))
print(abs(-2))
print(math.floor(4.5))
print(math.ceil(4.1))
# 保留几位小数，进行四舍五入 round(数字,n)n保留N小数
f=49.887
print(round(f,2))
print(round(f,0))
print(round(44.88,-1))

#返回随机数0~1实数random.random()
print(random.random())
#随机返回某个范围整数
print(random.randint(1,100))

# 使用函数str() 避免类型错误
age = 23
message = "Happy " + str(age) + "rd Birthday"
print(message)



