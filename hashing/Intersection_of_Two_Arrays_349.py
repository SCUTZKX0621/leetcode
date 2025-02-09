# -*- coding:utf-8 -*-
"""
作者：Zhakx
日期：2025年02月08日
"""


class Solution:
    @staticmethod
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if not nums1 or not nums2:
            return []
        list1 = set(nums1)
        result = []
        for num in nums2:
            if num in list1:
                result.append(num)
                list1.remove(num)
        return result

    def test(self):
        print(349)

