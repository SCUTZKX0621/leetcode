# -*- coding:utf-8 -*-
"""
作者：Zhakx
日期：2025年03月21日
"""
from math import comb


class Solution:
    def uniquePaths1(self, m: int, n: int) -> int:
        return comb(m + n - 2, n - 1)

    def uniquePaths2(self, m: int, n: int) -> int:
        matrix = [[0] * n for _ in range(m)]
        for i in range(n):
            matrix[0][i] = 1
        for j in range(m):
            matrix[j][0] = 1
        for q in range(1, m):
            for k in range(1, n):
                matrix[q][k] = matrix[q - 1][k] + matrix[q][k - 1]
        return matrix[m - 1][n - 1]

# 动态规划考虑以下问题：
#  1. dp数组以及下标的含义————matrix[i][j]表示走到第i-1行和j-1列的格子的方法数
#  2. 递推公式————matrix[q][k] = matrix[q - 1][k] + matrix[q][k - 1]
#  3. dp数组如何初始化————第0行和第0列全都为1
#  4. 遍历顺序是什么样（二维数字先i还是先j）————都可以
#  5. 打印数组