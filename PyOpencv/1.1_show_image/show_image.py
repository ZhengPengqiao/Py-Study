#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2 as cv

fname = '../assert/lena.jpg'

print(cv.__version__)

im = cv.imread(fname)
cv.imshow('image', im)
while True:
    k = cv.waitKey(0)

    if k == 27:
        print('ESC')
        cv.destroyAllWindows()
        break
