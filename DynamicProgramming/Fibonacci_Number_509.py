# -*- coding:utf-8 -*-
"""
作者：Zhakx
日期：2025年03月08日
"""


class Solution:
    def fib1(self, n: int) -> int:
        if n < 2:
            return n
        else:
            p, q, r = 0, 0, 1
            for _ in range(2, n + 1):
                p, q = q, r
                r = p + q
            return r
# 时间复杂度O(n)
# 空间复杂度O(1)

    def fib2(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        a = [0]*(n+1)
        a[0] = 0
        a[1] = 1
        for i in range(2, n + 1):
            a[i] = a[i-1] + a[i-2]
        return a[n]

# 时间复杂度O(n)
# 空间复杂度O(n)

# 动态规划考虑以下问题：
#  1. dp数组以及下标的含义
#  2. 递推公式
#  3. dp数组如何初始化
#  4. 遍历顺序是什么样（二维数字先i还是先j）
#  5. 打印数组