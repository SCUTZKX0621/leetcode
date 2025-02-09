# -*- coding:utf-8 -*-
"""
作者：Zhakx
日期：2025年02月08日
"""


class Solution:
    @staticmethod
    def isAnagram1(self, s: str, t: str) -> bool:
        record = [0] * 26
        for le in s:
            record[ord(le) - ord('a')] += 1
        for le in t:
            record[ord(le) - ord('a')] -= 1
        for num in record:
            if num != 0:
                return False
        return True

    @staticmethod
    def isAnagram2(s: str, t: str) -> bool:
        # 对字符串s中的字符进行排序，并将排序后的字符连接成一个新的字符串
        return "".join(sorted(s)) == "".join(sorted(t))

    def test(self):
        print(242)
