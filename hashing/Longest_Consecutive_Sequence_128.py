# -*- coding:utf-8 -*-
"""
作者：Zhakx
日期：2025年02月22日
"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        res = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                current = 1
                current_num = num
                while current_num + 1 in nums_set:
                    current_num += 1
                    current += 1
                res = max(current, res)
        return res

# 时间复杂度 O（n）
