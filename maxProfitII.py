#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:maxProfitII.py
# @Author: Michael.liu
# @Date:2020/7/22 16:41
# @Desc: this code is ....

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro =0
        i =1
        while i < len(prices):
            profit = prices[i] -prices[i-1]
            if profit > 0:
                maxPro +=profit
            i +=1
        return maxPro