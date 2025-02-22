# -*- coding:utf-8 -*-
"""
作者：Zhakx
日期：2025年02月22日
"""


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(c ** 0.5)
        while left <= right:
            sum = left * left + right * right
            if sum > c:
                right -= 1
            elif sum < c:
                left += 1
            else:
                return True
        return False

# 时间复杂度 O(sqrt(c))