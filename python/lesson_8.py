# -*- coding: utf-8 -*-
# @Author: wxiangbo
# @Date:   2016-05-02 16:57:01
# @Last Modified by:   wxiangbo
# @Last Modified time: 2016-05-02 18:36:33
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