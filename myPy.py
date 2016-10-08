#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
a = 'abc'
b = a
a = 'xyz'
print(a)
print u'中文'
"""
classmate =['Bob','Cindy','Mike']
print len(classmate)
print classmate[2]
classmate.insert(0,'Amy')
print classmate
classmate.pop()
print classmate
classmate1 = (1,(1,2))
print classmate1[1][1]

sum = 0
a = int(raw_input())
for x in range(a):
    sum = sum + x
print sum
