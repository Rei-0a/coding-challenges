# Problem: https://leetcode.com/problems/two-sum/description/
# Difficulty: Easy
# Date: 2025-06-21

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