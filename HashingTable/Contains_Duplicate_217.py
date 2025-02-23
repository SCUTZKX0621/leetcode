# -*- coding:utf-8 -*-
"""
作者：Zhakx
日期：2025年02月24日
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
# python用哈希的做法不如直接这样利用set的去重性质

# set之间的计算

# s1 = set([1, 2, 3])
# s2 = set([4, 2, 3])
# print(s1 | s2) 1 2 3 4
# print(s1 & s2) 2 3
# print(s1 - s2) 1
