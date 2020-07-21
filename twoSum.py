#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:twoSum.py
# @Author: Michael.liu
# @Date:2020/7/13 12:57
# @Desc: this code is ....
from _ast import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    print("this is the firest codes")
    if len(nums) == 0:
       return [-1]
    else:
       for i in range(len(nums)):
           if (target - nums[i]) in nums:
               num = target - nums[i]
               if num in nums[i + 1:]:
                    return [i, nums.index(num, i + 1)]