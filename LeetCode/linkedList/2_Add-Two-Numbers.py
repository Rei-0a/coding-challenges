# Problem: https://leetcode.com/problems/add-two-numbers/description/
# Difficulty: Medium
# Date : 2025-06-22


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        num1 = 0
        num2 = 0
        count = 0
        while True:
            num1 += l1.val*10**count
            count += 1
            if l1.next == None:
                break
            else:
                l1 = l1.next
        
        count = 0
        while True:
            num2 += l2.val*10**count
            count += 1
            if l2.next == None:
                break
            else:
                l2 = l2.next
        dis = str(num1 + num2)
        ans = pre_node = ListNode(int(dis[0]))    # 一番最下位のノードを最初に保存しておく
        print(ans)
        for i in dis[1:]:    # 下から2番目のノードから順にリストへ格納
            ans = ListNode(int(i),pre_node)
            pre_node = ans

        return ans