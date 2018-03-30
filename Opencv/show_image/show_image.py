#!/usr/bin/python
# -*- coding: utf-8 -*-

# 应该使用python2.7

import cv2 as cv

fname = '../assert/lena.jpg'

im = cv.imread(fname)
cv.imshow('image', im)
while True:
    k = cv.waitKey(0)

    if k == 27:
        print('ESC')
        cv.destroyAllWindows()
        break
