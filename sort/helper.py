#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:helper.py
# @Author: Michael.liu
# @Date:2020/7/22 14:42
# @Desc: this code is ....
import random

def randomList(n):
    iList = []
    for  i in range(n):
        iList.append(random.randrange(1000))
    return iList
