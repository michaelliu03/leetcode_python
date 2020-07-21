#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:romanToInt.py
# @Author: Michael.liu
# @Date:2020/7/21 20:17
# @Desc: this code is ....

class Solution:
    def romanToInt(self, s: str) -> int:
        result =0
        flag = 0
        dict1 = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        dict2 = {'CM':900,'CD':400,'XC':90,'XL':40,'IX':9,'IV':4}

        length = len(s)
        for i in range(length -1):
            if flag == 1:
                flag =0
                continue
            if s[i] + s[i+1] in dict2:
                result += dict2[s[i] + s[i+1]]
                flag = 1
            else:
                result += dict1[s[i]]
        if flag ==0 :
            result +=dict1[s[length-1]]

        return result