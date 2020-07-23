#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:maxProfitI.py
# @Author: Michael.liu
# @Date:2020/7/22 16:39
# @Desc: this code is ....

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        n = len(prices)
        dp = [[0 for i in range(2)] for i in range(n)]
        dp[0][0] =0
        dp[0][1] = -prices[0]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1],-prices[i])
        return dp[n-1][0]