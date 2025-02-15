# -*- coding:utf-8 -*-
"""
作者：Zhakx
日期：2025年02月16日
"""

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle1(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while not fast and not fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False