#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:bubbleSort.py
# @Author: Michael.liu
# @Date:2020/7/22 13:15
# @Desc: this code is ....

from sort.randomList import *
import timeit


iList = randomList(20)

def bubbleSort(iList):
    if len(iList)  <= 1:
        return iList
    for i in range(1,len(iList)):
        for j in range(0,len(iList)-1):
            if iList[j] > iList[j+1]:
                iList[j],iList[j+1] = iList[j+1],iList[j]
        print("%d loop sort result" %i,end="")
        print(iList)
    return iList