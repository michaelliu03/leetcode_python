#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:rotate.py
# @Author: Michael.liu
# @Date:2020/7/22 16:53
# @Desc: this code is ....
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        nums.reverse()
        k = k % len(nums)
        while k > 0:
            temp = nums.pop(0)
            nums.append(temp)
            k-=1
        nums.reverse()
        return
