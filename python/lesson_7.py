# -*- coding: utf-8 -*-
# @Author: wxiangbo
# @Date:   2016-05-02 14:46:25
# @Last Modified by:   wxiangbo
# @Last Modified time: 2016-05-02 16:55:46
### 内置对象类型 ###
#数字 1234
#字符串 'spam'
#列表 [1,2,3]
#字典 {'food':'spam'}
#元组 (1,2,'spam')
#文件 file = open('eggs','r')
#集合 set('abc'),{'a','b','c'}
#其他类型 类型 None 布尔型
#编程单元类型 函数 模块 类
print(2 ** 10)
print(len(str(2 ** 10)))
import math
print(math.pi)
print(math.sqrt(9))

import random
print(math.ceil(random.random() * 10)) #math.floor 舍去法取整 math.ceil进一法取整
print(random.choice([1,2,3,4]))

#字符串
s = 'spam'
print(s)
print(len(s))
print(s[0]) #s
print(s[-1]) #m
#print(s[5]) #报错
#
print(s[0:3])
print(s[:-2])
s = 'z' + s[:]
print(s) # zspam
print(s.find("z")) # 0

print(s.find('b')) # 找不到b会返回-1
print(s.replace("am","xy")) #zspxy

abc = "a,b,c,d"
print(abc.split(",")) # 将abc用逗号分割为列表
print(abc.upper()) # 将变量abc转为大写
print(abc.isalpha()) # 字符串abc是否全是字母
print("abc".isalpha()) # true

print("abc\n".rstrip()) # 去掉换行符
# 格式化高级替代
print("%s,eggs,and %s" % ("a","b")) # a,eggs and b
print("%d eggs and b" % (12)) # 12 eggs and b

print('{0} eggs' . format(12)) # 12 eggs

# 字符串函数方法
st = "abc";
print(st.index("a")) # 获取a的索引
print(st.index("ab"))

print(help(st.index)) # 如果找不到会返回异常而不是-1
#print(st.index('x')) # substring not found
print(st.capitalize()) # 将字符串的第一个字符转为大写
print("3abc".capitalize()) #如果第一个字符不是字母则不转换
print(help(st.center))
print("ddd".center(12,'a')) #将原有字符串居中，然后用指定字符串填充到指定数量的字符
print("ddddddd".count('d',0,2)) # 2 返回字符串d在字符串里指定索引内出现的次数
print("ddddd".encode("utf-8")) #将字符串转换为utf-8 unicode编码
print("dd44gg".islower()) #是否全为小写字母 true
print("dd55gg".isnumeric()) # 是否全为数字 false
listss = ['a','b','c']
print(''.join(listss)) # 将列表连接成字符串 可将序列中的元素用指定字符串连接成字符串
a = ['2016','5','2'] #必须为字符串
print('-'.join(a)) # 2016-5-2