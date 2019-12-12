# -*- coding: utf-8 -*-
'''
@File    :   number.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2019/12/11 10:47 
'''
# 数字 Number

# 常用函数 int()
# 		float()
# 		complex()
# 		abs()返回绝对值
# 		math.ceil()向上取整数
# 		math.floor()向下取整数
# 		random.random()生成0到1的随机实数
# 		random.randint()生成某个区间的随机整数

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

# 返回整型  整除
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

a = 2
a = a * 3
# 也可以写成
a *= 3


# 限制小数点格式化输出
PI =math.pi
print('常量PI的值近似于%.2f' % (PI))
print('常量PI的值近似于{:.2f}'.format(PI))
print(f'常量PI的值近似于{PI:.2f}') # 3.6的语法糖 我选择用这个吧



# 使用函数str() 避免类型错误
age = 23
message = "Happy " + str(age) + "rd Birthday"
print(message)
print(f'祝你{age}岁生日快乐')



