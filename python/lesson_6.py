# -*- coding: utf-8 -*-
# @Author: wxiangbo
# @Date:   2016-04-28 17:00:00
# @Last Modified by:   wxiangbo
# @Last Modified time: 2016-05-02 14:45:10
print(17 // 3) #两个斜线可以丢掉小数
print('spam' * 8)
import os
print(os.getcwd()) # 获取当前路径
import sys
print(sys.platform) #软件平台
print(2 ** 100) #2的100次方
x = 'spam'
print(x * 8)
#input() # 在windows下程序不会一闪而过，而会等待继续输入 按enter可以退出

#exec(open('lesson_6.py').read()) # 执行lesson_6.py里的代码,open('文件',encoding='utf-8') 可以指定文件路径和编码
#
#python学习手册习题
#1.cmd下输入python即可进入交互式解释器会话
#2.cmd python
L = [1,2]
L.append(L)
print(L)