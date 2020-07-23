#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:removeDuplicates.py
# @Author: Michael.liu
# @Date:2020/7/22 15:49
# @Desc: this code is ....

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n =len(set(nums))
        i =0
        while i < n-1:
            if nums[i] == nums[i+1]:
                temp = nums[i+1]
                nums[i+1:len(nums)-1] = nums[i+2:]
                nums[-1] = temp
                continue
            else:
                i+=1
        return n