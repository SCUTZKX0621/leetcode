# -*- coding:utf-8 -*-
"""
作者：Zhakx
日期：2025年03月30日
"""


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1) # dp[i]表示i个结点可以构成的二叉搜索树的数量
        # 初始化
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j] # 递推公式
        return dp[n]