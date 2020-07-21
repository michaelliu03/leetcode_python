#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:numTrees.py
# @Author: Michael.liu
# @Date:2020/7/21 20:42
# @Desc: this code is ....
class Solution:
    def numTrees(self, n: int) -> int:
        res = [0] * (n + 1)
        res[0] = 1
        res[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                res[i] += res[j - 1] * res[i - j]
        return res[-1]