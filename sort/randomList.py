#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:randomList.py
# @Author: Michael.liu
# @Date:2020/7/22 13:12
# @Desc: this code is ....
import random
from sort.bubbleSort import  *
from sort.helper import *
from sort.selectionSort import selectionSort
import timeit



if __name__ =="__main__":
    iList = randomList(10)
    print(iList)
    print(bubbleSort(iList))
    print(timeit.timeit("bubbleSort(iList)","from __main__ import bubbleSort,iList",number=100))

    print("=========selection=========")
    print(selectionSort(iList))
    print(timeit.timeit("selectionSort(iList)","from __main__ import selectionSort,iList",number=100))
