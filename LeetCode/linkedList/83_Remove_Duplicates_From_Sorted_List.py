# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
# Difficulty: Easy
# Date: 2025-07-03

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        while current and current.next:
            num = current.val
            if (current.next).val == num:     # 次のノードの値が今のノードの値と一緒のとき
                current.next = current.next.next
            else:
                current = current.next
        
        return head