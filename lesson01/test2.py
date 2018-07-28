#!/usr/bin/env python
# coding=utf-8

## 理解python引用
#a = 10
#b = a
#print id(a), id(b), id(10)
#b = 20
#print id(20), id(b)

## python支持if...else...  elif..
#if expression:
#    do_something1
#else:
#    do_something2

## while循环
#counter = 0
#while counter < 3:
#    print 'loop %d' %counter
#    counter += 1

## for循环
#mystr = 'abcd'
#for c in mystr:
#    print c
#a = [1,2,3,4]
#for item in a:
#    print item
#
#b = {
#        'key1':'value1', 
#        'key2':'value2',
#        'key3':'value3'
#}
#
#for key in b:
#    print key
## 区间前闭后开
#for i in range(0,10):
#    print i

## 查找1~99第一个3的倍数, for循环不影响变量的作用域
#for i in range(1,100):
#    if(i % 3 == 0):
#        break
#print i
#for i in range(1,100):
#    if i % 3 != 0:
#        continue
#    print i

#a = []
#for x in range(4):
#    a.append(x ** 2)
#print a

## 列表推导
#a = [x ** 2 for x in range(4)]
#print a

#a = [x ** 2 for x in range(100) if x % 2 == 1]
#print a

## 函数
#def Add(x, y):
#    return x + y
#
#print Add(1, -1)
#
#print Add('hello', 'world')
## 错print Add(3, 'hello')

## python不支持函数重载，后定义的同名函数会覆盖前面的函数
#def Func():
#    print 'aaa'
#
#def Func(x):
#    print 'bbb'
#print type(Func)
#Func()

#def GetPoint():
#    x = 10
#    y = 20
#    return x, y
#a, b = GetPoint()
#_, b = GetPoint()
#print b
#print type(GetPoint())

# 文件操作
# f是文件对象
#f = open('test.txt', 'r')
#for line in f:
#    print line,
#f.close()
#
#data = {}
#f = open('test.txt', 'r')
#for word in f:
#    if word in data:
#        data[word] += 1
#    else:
#        data[word] = 1
#f.close()
#
#print data

# add.pyc 是.py编译后的结果
# import add
# print add.Add(10, 20)
#import sys
#print sys.path

# 报复社会之离职代码
#True, False = False, True
#if True:
#    print 'hehe'
#else:
#    print 'haha'

#def Func():
#    x = 10
#    print locals()
#    print globals()
#    return x
#Func()
#print Func() 


#文档字符串
#def Add(x, y):
#    '求两个对象相加的结果'
#    return x + y
#
#print Add.__doc__
# help(Add)

import add
help(add.Add)















