# -*- coding: utf-8 -*-
# @Author: wxiangbo
# @Date:   2016-05-23 22:56:17
# @Last Modified by:   wxiangbo
# @Last Modified time: 2016-05-23 23:15:45
squares = [x ** 2 for x in [1,2,3]]
print(squares)
squares = []
for x in [1,2,4]:
    squares.append(x ** 2)
print(squares)

D = {'a':1,'b':2}
if not 'a' in D:
    print('exists')
else:
    print('missing')

print(D.get('a','c')) # true 如果列表D里存在健为a的值，那么就返回a对应的值,不存在就返回c
print(D.get('c','haah'))

#另一种获取的方法是
val = D['x'] if 'x' in D else 0 #0
print(val)

#########元祖
T = (1,2,4,5,6)
print(len(T))
print(T + (7,8))

print(T)  #尽管上面在元祖里加了7,8,但是元祖不可变
print(T.index(2)) # 4 获取索引为2的值 xxxxxxxxxxxxxxxxxxx