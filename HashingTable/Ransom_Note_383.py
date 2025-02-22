# -*- coding:utf-8 -*-
"""
作者：Zhakx
日期：2025年02月16日
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        for s in ransomNote:
            if s in magazine:
                magazine = magazine.replace(s, '', 1)
                continue
            return False
        return True

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        if len(ransomNote) > len(magazine):
            return False
        return not Counter(ransomNote) - Counter(magazine)
