# -*- coding:utf-8 -*-
"""
作者：Zhakx
日期：2025年03月20日
"""


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        res = [0] * (n + 1)
        for i in range(2, n + 1):
            res[i] = min(res[i-1] + cost[i-1], res[i-2]+cost[i-2])
        return res[n]

# 爬到第n节楼梯，要么从n-1节往上爬1节，要么n-2节往上爬两节，最小开销就是res[i-1] + cost[i-1]和res[i-2]+cost[i-2]更小的
# 动态规划五步法
# 1. 数组下标含义 res[i] 表示爬到第i节楼梯的最小开销，对于cost数字，i为0到n-1，res数组要多一个，因为要爬出去
# 2. 递推公式：如上
# 3. 初始化：第0和1节直接上，不用开销，就是0，从第2节开始要靠前两个结果
# 4. 遍历顺序，只有知道前面的才能算出后面的，所以遍历顺序是从前到后
# 5. 打印数组
