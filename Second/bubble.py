# -*- coding: utf-8 -*-
'''
@File    :   c.py
@Contact :   18898513573
@Author  :   DrewB
@Time    :   2019/12/15 10:43
'''
# 冒泡 Bublle


'''
定义一个List（列表），任意输入10个数字保存到List,然后按从小到大排序（冒泡排序）
'''
print('请输入10个任意数字！按回车键结束')
lis = []  # 定义一个空列表
for x in range(1, 3):  # 从1开始到10结束，共10个数字，符合题意
    num = int(input(f'请你输入第{x}个数字：'))  # 定义输入数字为number型并赋值给变量num
    lis.append(num)  # 将变量num值添加给空列表lis


# 第一种方法：冒泡排序--从左往右推
# temp=0#将0赋值给temp
# lis = [5, 9, 40, 80, 60, 22, 25, 65, 31, 1]
# A0B3 lis=[5, 9, 40, 60, 80, 22, 25, 65, 31, 1]
# A0B4 lis=[5, 9, 40, 60, 22, 80, 25, 65, 31, 1]
for a in range(len(lis)):  # 循环lis列表中输入的数据，有多少个就循环多少次
    # len(10) range(10) 0~9  A0
    for b in range(len(lis) - 1):  # 在外循环一次时，就执行第二个for语句。并且将列表lis减一个返回给b
        # len(9) range(9) 0~8

        if lis[b] < lis[b + 1]:  # 进行比较。如题返回b值的大于lis[b]，就把lis[b]的值赋值给temp
            # A0B0 lis[0] = 5, lis[1] = 9
            # A0B1 lis[1] = 9, lis[2] = 40
            # A0B2 lis[2] = 40,lis[3] = 80
            # A0B3 lis[3] = 80,lis[4] = 60
            # A0B4 lis[4] = 80,lis[5] = 22

            lis[b], lis[b + 1] = lis[b + 1], lis[b]  # 对调  80, 60 = 60, 80
            #       80, 22 = 22, 80
            # A0B3 lis[3] = 60, lis[4] = 80
            # A0B4 lis[4] = 22, lis[5] = 80

print(lis)

# 第二种方法：冒泡排序--从右往左推

'''
for a in range(len(lis)): #  循环90次 len(lis) = 10, range(0,10,1) = 0~9 A0
    for b in range(len(lis)-1,0,-1): # len(9,0,-1) 9~1 (9,8,7,6,5,4,3,2,1) B9

        if lis[b] < lis[(b)-1]: # A0B9 lis[9]=25,lis[(9)-1] = 90 True
                                # A0B8 lis[8]=25,lis[(8)-1] = 100 True

              lis[b],lis[b-1]=lis[b-1],lis[b] # 25, 90 = 90, 25
                                              # 25，100 = 100，25
            # lis[9] = 90 lis[8] = 25
            # lis[8] = 100 lis[7] = 25
print(lis)

'''
testlist = [1,100,9,22,80,30,23,86,38]

def bubble_sort(alist):
    '''冒泡排序'''
    n = len(alist)

    for i in range(n):
        for j in range(n - 1):
            if alist[j] > alist[j + 1]:

                alist[j], alist[j + 1] = alist[j + 1], alist[j]
    print(alist)

bubble_sort(testlist)
