# Problem: https://leetcode.com/problems/contains-duplicate/description/
# Difficulty: Easy
# Date: 23/06/2025

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_hash = {}
        for num in nums:
            if num in num_hash:
                return True
            num_hash[num] = 1
        return False