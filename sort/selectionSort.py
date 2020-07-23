#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:selectionSort.py
# @Author: Michael.liu
# @Date:2020/7/22 13:27
# @Desc: this code is ....
from sort.randomList import *
import timeit



iList = randomList(20)

def selectionSort(iList):
    if len(iList) <=1:
        return
    for i in range(0,len(iList)-1):
        if iList[i] != min(iList[i:]):
            minIndex = iList.index(min(iList[i:]))
            iList[i],iList[minIndex] = iList[minIndex],iList[i]
        print("%d loop sort result" %(i+1),end="")
        print(iList)
    return iList
