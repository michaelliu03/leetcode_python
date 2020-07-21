#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:removeElement.py
# @Author: Michael.liu
# @Date:2020/7/21 20:33
# @Desc: this code is ....
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = len(nums)
        if l ==0:
            return 0
        i=0
        while i < l:
            if nums[i] == val:
                nums.pop(i)
                l-=1
            else:
                i+=1
        return len(nums)