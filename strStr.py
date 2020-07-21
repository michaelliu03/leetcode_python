#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:strStr.py
# @Author: Michael.liu
# @Date:2020/7/21 20:33
# @Desc: this code is ....
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle :
            return 0
        l1 = len(haystack)
        l2 = len(needle)

        if l1 < l2:
            return -1

        l = l1 -l2 +1
        for i in range(l):
            if haystack[i:i+l2] == needle:
                return i
        return -1