# -*- coding: utf-8 -*-
'''
@File    :   Practice.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2020/2/9 19:18 
'''
def display_message():
    print('hello')
display_message()

def favorite_book(title):
    print(f'One of my favorite books is {title} in Wonderland')

favorite_book('Mengc')

def make_shirt(size, text = 'I love python'):

    print(f'\nThis shirt size is {size}')
    print(f'shirt text is {text}')

make_shirt('X')

def city_country(city, country):

    full = city + "," + country
    return  full.title()

ccone = city_country('Beijing', 'China')
cctow = city_country('NewYok', 'USA')
ccthree = city_country('Dongjing', 'Jb')
print(ccone)
print(cctow)
print(ccthree)

def make_ablum(name, musicname, musicnum=''): # musicnum 为默认值

    music = {'name':name, 'musicname':musicname}
    if musicnum:
        music['musicnum'] = musicnum

    return music

music1 = make_ablum('dzq','aiai')
music2 = make_ablum('zjl','qiqiq')
music3 = make_ablum('iii','wow')
music4 = make_ablum('woe','weiow', 3)
print(music1)
print(music2)
print(music3)
print(music4)

magicians = ['lala', 'bubu', 'ccc', 'dede']


def show_magician(magicians):
    '''输出魔术师名字'''
    for magician in magicians:
        print(f'the Great {magician}')
show_magician(magicians[:])

for magi in magicians:
    print(magi)

