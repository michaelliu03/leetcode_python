#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:generateTrees.py
# @Author: Michael.liu
# @Date:2020/7/21 20:07
# @Desc: this code is ....
from TreeNode import *

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n==0:
            return []
        def helper(start,end):
            res = []
            if start > end:
                res.append(None)
            for val in range(start,end +1):
                for left in helper(start, val-1):
                    for right in helper(val+1,end):
                        root = TreeNode(val)
                        root.left = left
                        root.right = right
                        res.append(root)
            return res
        return helper(1,n)