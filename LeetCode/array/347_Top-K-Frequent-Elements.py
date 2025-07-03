# Problem: https://leetcode.com/problems/top-k-frequent-elements/description/
# Difficulty: Medium
# Date: 2025-06-23

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums.sort()
        nums_count = {}
        index = 0
        while True:
            num = nums[index]   # 数字を保存
            count = 0           # その数字がいくつあるかを数える
            while index < len(nums) and nums[index] == num:
                count += 1
                index += 1

            nums_count[num] = count
            if index == len(nums):
                break

        nums_count = sorted(nums_count.items(), key = lambda x:x[1], reverse = True)
        ranking_k = []
        for rank in range(k):
            ranking_k.append(nums_count[rank][0])

        return ranking_k

