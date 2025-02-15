# -*- coding:utf-8 -*-
"""
作者：Zhakx
日期：2025年02月15日
"""


class Solution:
    # 确定不会无穷计算下去，一定会到1或者成环
    def isHappy(self, n: int) -> bool:
        def getNext(num):
            sum = 0
            while num != 0:
                temp = num % 10
                sum += temp * temp
                num = int(num / 10)
            return sum
        slow = n
        fast = getNext(n)
        while fast != 1 and fast != slow:
            slow = getNext(slow)
            fast = getNext(getNext(fast))
        return fast == 1

# 时间复杂度O(log n)