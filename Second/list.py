# -*- coding: utf-8 -*-
'''
@File    :   list.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2019/12/12 9:23 
'''
import sys

'''
数据结构（Data Structures）基本上人如其名——它们只是一种结构，能够将一些数据聚合在一起。换句话说，它们是用来存储一系列相关数据的集合。
Python 中有四种内置的数据结构——列表（List）、元组（Tuple）、字典（Dictionary）和集合（Set）。我们将了解如何使用它们，并利用它们将我们的编程之路变得更加简单。
列表
列表 是一种用于保存一系列有序项目的集合，也就是说，你可以利用列表保存一串项目的序列。想象起来也不难，你可以想象你有一张购物清单，上面列出了需要购买的商品，除开在购物清单上你可能为每件物品都单独列一行，在 Python 中你需要在它们之间多加上一个逗号。
项目的列表应该用方括号括起来，这样 Python 才能理解到你正在指定一张列表。一旦你创建了一张列表，你可以添加、移除或搜索列表中的项目。既然我们可以添加或删除项目，我们会说列表是一种可变的（Mutable）数据类型，意即，这种类型是可以被改变的。
'''
# list 列表
shoplist = ['apple', 'mango', 'banana', 'carrot']
print('I have', len(shoplist), 'Items to purchase.')
print('the Items are:', end='')
for items in shoplist:
    print(items, end=' ')  # 输出列表中全部元素
print('\nI also buy some rice')
shoplist.append('rice')   # 往列表最后添加元素
print('my shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()  # 重新排列列表
print('Sorted shopping list is', shoplist)

print('The first item I will buy is ', shoplist[0]) # 获取列表第一个元素
olditem = shoplist[0]  # 把列表第一个元素赋值给olditem
del shoplist[0]  # 删除列表第一个元素
print('I bought the', olditem)
print('My shopping list is now', shoplist)

list1 = [1, 3, 5, 7, 100]
# 添加元素
list1.append(200)
list1.insert(1, 400)
# 合并两个列表
list1.extend([1000, 2000])

list1 += [1000, 2000]

print(list1)
print(len(list1))

# 先通过成员运算判断元素是否在列表中，如果存在就删除元素
if 3 in list1:
    list1.remove(3)
if 1234 in list1:
    list1.remove(1234)

print(list1)

# 从指定位置删除元素
list1.pop(0)
list1.pop(len(list1) - 1)

print(list1)
# 清空列表元素
list1.clear()
print(list1)

# 和字符串一样，列表也可以做切片操作，
# 通过切片操作我们可以实现对列表的复制或者将列表中的
# 一部分取出来创建出新的列表，代码如下所示。

fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
# 列表切片
fruits2 = fruits[1:4]
print(fruits2)
# 可以通过完整切片操作来复制列表
fruits3 = fruits2[:]
print(fruits3)

fruits4 = fruits[-3: -1]
print(fruits4)
# 可以通过反向切片操作来获得倒转后的列表的拷贝
fruits5 = fruits[:: -1]
print(fruits5)

# 对列表的排序操作。

list1 = ['orange', 'apple', 'zoo', 'internationalization', 'buleberry']
lsit2 = sorted(list1)
# sorted 函数返回列表排序后的拷贝 不会修改传入的列表
# 函数的设计就应该像sorted 函数一样，尽可能不产生副作用
list3 = sorted(list1, reverse=True)

# 通过key 关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len)
print(list1)
print(lsit2)
print(list3)
print(list4)
# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list)

# 生成式和生成器
# 使用列表生成式语法来创建列表

f = [x for x in range(1, 10)]  # 用for in 循环来创建列表x  空格分开
print(f)  # [1,~9]
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)  # f[A1,A2,~A6~E7]
# 用列表的生成表达式语法创建列表窗口
# 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
f = [x ** 2 for x in range(1, 10)]
print(sys.getsizeof(f))  # 查看对象占用内存的字节数

print(f)

# 请注意下面的代码创建的不是一个列表而是一个 生成器对象
# 通过生成器可以获取到数据但它不占用额外的空间存储数据
# 每次需要数据的时候就通过内部的运算得到数据（需要额外的时间）
f = (x ** 2 for x in range(1, 10))
print(sys.getsizeof(f))  # 相比生成式 生成器不占用存储数据的空间

print(f)

for val in f:
    print(val)


# Python中还有另外一种定义生成器的方式，
# 就是通过yield关键字将一个普通函数改造成生成器函数。
# 下面的代码演示了如何实现一个生成斐波拉切数列的生成器。
# 所谓斐波拉切数列可以通过下面递归的方法来进行定义：

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b  # 之后的数由 前面的两个数相加
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()

