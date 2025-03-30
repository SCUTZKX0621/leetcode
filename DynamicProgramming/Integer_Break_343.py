# -*- coding:utf-8 -*-
"""
作者：Zhakx
日期：2025年03月30日
"""


class Solution:
    def integerBreak(self, n: int) -> int:
        my_list = [0 for _ in range(n + 1)]
        my_list[1] = 1
        my_list[2] = 1
        for i in range(3, n + 1):
            for j in range(1, i // 2 + 1):
                my_list[i] = max(my_list[i - j] * j, (i - j) * j, my_list[i])
        return my_list[n]

