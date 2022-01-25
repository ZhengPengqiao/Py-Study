#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import calendar

print ("Hello world")

cal = calendar.month(2016, 1)

print ("日历(2016,1):")
print (cal)

timeVal = time.time()
print ("当前时间:", timeVal)
print ("当前时间:", time.localtime(timeVal))

for letter in 'Python':
    print ('Current Later', letter)

fruites = ['banna', 'apple', 'mango']

for fruite in fruites:
    print ("我喜欢吃:", fruite)

if __name__ == '__main__':
    print ("you direct runing this python file")
