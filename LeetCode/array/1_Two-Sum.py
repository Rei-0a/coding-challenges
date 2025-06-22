# Problem: https://leetcode.com/problems/two-sum/description/
# Difficulty: Easy

'''
Jun/21/2025

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

'''

# numsとtargetが与えられる

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = [] # 出力
        for i in range(len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    output.append(i)
                    output.append(j)
        return output