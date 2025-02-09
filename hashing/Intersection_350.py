# -*- coding:utf-8 -*-
"""
作者：Zhakx
日期：2025年02月10日
"""


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        from collections import Counter
        return list((Counter(nums1) & Counter(nums2)).elements())
        # 举个例子
        # nums1 = [1, 2, 3, 4, 4]
        # nums2 = [1, 2, 2, 3, 4]
        # Counter(nums1) Counter({ 1: 1, 2: 1, 3: 1, 4: 2})
        # Counter(nums2) Counter({ 1: 1, 2: 2, 3: 1, 4: 1})
        # 取交集 Counter({ 1: 1, 2: 1, 3: 1, 4: 1}
        # element方法，依次输出，再转为list
        # 时间复杂度：O(n + m)，其中 n 和 m 分别是 nums1 和 nums2 的长度。


