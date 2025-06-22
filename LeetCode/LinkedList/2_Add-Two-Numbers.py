# Problem: https://leetcode.com/problems/add-two-numbers/description/
# Difficulty: Medium

'''
22/June/2025

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

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