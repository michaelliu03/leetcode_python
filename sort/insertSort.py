#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:insertSort.py
# @Author: Michael.liu
# @Date:2020/7/22 14:45
# @Desc: this code is ....
from sort.helper import *
import timeit

iList = randomList(20)

def insertSort(iList):
    if len(iList) <=1:
        return iList
    for right in range(1,len(iList)):
        target = iList[right]
        for left in range(0,right):
            if target <=iList[left]:
                iList[left+1:right+1] = iList[left:right]
                iList[left] = target
                break
        print("%d loop sort res"%(right),end="")
        print(iList)
    return iList

if __name__ =="__main__":
    print(iList)
    print(insertSort(iList))
    print(timeit.timeit("insertSort(iList)","from __main__ import insetSort,List",number=100))
