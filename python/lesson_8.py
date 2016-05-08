# -*- coding: utf-8 -*-
# @Author: wxiangbo
# @Date:   2016-05-02 16:57:01
# @Last Modified by:   wxiangbo
# @Last Modified time: 2016-05-08 14:38:47
#编写字符串的其他方法
msg = """ abcd
efffdfsfdsa"""
print(msg)

print("abc\n\"") # \转义字符
#模式匹配
import re
match = re.match('Hello[\t]*(.*)world','Hello Python world')
print(match.group(1))
match = re.match('/(.*)/(.*)/(.*)',"/usr/home/luberjack")
print(match.groups())

#列表
L = [1,23,'a']
print(len(L)) # 3
print(L[1]) # 123
print(L + [4,5,6])

print(L[:2])
L.append('NI') # 1,23,a,NI
print(L)
print(L.pop(2)) # 弹出索引为2的元素
L.insert(1,'abc') #在索引1之前插入字符串abc
print(L)
L.remove('abc') #移除值为abc的选项
print(L)

L.reverse() #字符串反转
print(L)
#列表嵌套
M = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(M)

#列表解析 （有点小的饶人）
new = [row[1] for row in M] #row in M 中row为M中的子元素,row[1] 即为每个子元素的索引1的元素
print(new) # [2,5,8]
print([row[1] * 2 for row in M]) # [4,10,16]

#列表解析加上表达式
print([row[1] for row in M if row[1]%2 == 0]) #如果row[1]是能被2整除才会放到列表

#步进
L = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12,13]
]
print([L[i][i] for i in [0,1,2,3]]) #[1,5,9,13] 依次取L的L[0][0],L[1][1],L[2][2]

G = (sum(row) for row in L)
print(next(G)) # 6
print(next(G)) # 15
print(list(map(sum,L)))
print({sum(row) for row in L}) #集合
print({i:sum(L[i]) for i in range(4)}) # 字典
print([ord(x) for x in 'spam']) # ord 可将字符串转为对应的asci码
print({x:ord(x) for x in 'spam'})

# 字典
D = {"food":"spam","name":"wxiangbo","age":29,'job':['a','b']}
print(D["food"])
print(D["age"] + 1)
D['job'].append('abcd')
print(D)