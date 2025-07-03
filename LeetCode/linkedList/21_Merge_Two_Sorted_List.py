# Problem: https://leetcode.com/problems/merge-two-sorted-lists/description/
# Difficulty: Easy
# Date: 2025-07-03

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        first = ListNode()
        merged = first
        while list1 and list2:
            if list1.val < list2.val: # list2が存在しない  or list1 < list2
                merged.next = list1
                list1 = list1.next
            else:
                merged.next = list2
                list2 = list2.next
            merged = merged.next

        # ここらへんは、
        # if list1:
        #     cur.next = list1
        # else:
        #     cur.ext = list2
        # で簡略化することができる✨
        while list1:
            merged.next = list1
            list1 = list1.next
            merged = merged.next
        while list2:
            merged.next = list2
            list2 = list2.next
            merged = merged.next
        
        return first.next
        