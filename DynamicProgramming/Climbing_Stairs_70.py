# -*- coding:utf-8 -*-
"""
作者：Zhakx
日期：2025年03月20日
"""
class Solution:
    def climbStairs1(self, n: int) -> int:
        if n <= 2:
            return n
        else:
            p, q, r = 0, 1, 2
            for _ in range(3, n + 1):
                p, q = q, r
                r = p + q
            return r

    def climbStairs2(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            res = [0] * (n + 1)
            res[0] = 1
            res[1] = 2
            for i in range(2, n + 1):
                res[i] = res[i - 1] + res[i - 2]
            return res[n - 1]