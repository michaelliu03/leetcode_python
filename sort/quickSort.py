#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:quickSort.py
# @Author: Michael.liu
# @Date:2020/7/22 15:36
# @Desc: this code is ....
from sort.helper import *
import timeit

iList = randomList(20)

def quickSort(iList):
    if len(iList) <=1:
        return iList
    left = []
    right =[]

    for i in iList[1:]:
        if i <=iList[0]:
            left.append(i)
        else:
            right.append(i)
    return quickSort(left) + [iList[0]] + quickSort(right)

if __name__ =="__main__":
    print(iList)
    print(quickSort(iList))
    print(timeit.timeit("quickSort(iList)","from __main__ import quickSort,iList",number=100))