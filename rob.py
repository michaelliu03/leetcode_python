#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:rob.py
# @Author: Michael.liu
# @Date:2020/7/21 19:55
# @Desc: this code is ....

class Solution:
    def rob(self, nums: List[int]) -> int:
        r = {}
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            r[0] = nums[0]
            r[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                r[i] = max(r[i - 1], r[i - 2] + nums[i])
        return r[len(nums) - 1]