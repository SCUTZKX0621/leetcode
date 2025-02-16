# -*- coding:utf-8 -*-
"""
作者：Zhakx
日期：2025年02月16日
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_to_t = {}  # 记录 s 到 t 的映射
        t_to_s = {}  # 记录 t 到 s 的映射
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            # 检查 s 到 t 的映射
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            else:
                s_to_t[char_s] = char_t
            # 检查 t 到 s 的映射
            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False
            else:
                t_to_s[char_t] = char_s
        return True

