# Problem: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
# Difficulty: Medium
# Date: 25/06/2025

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1

        while left <= right:
            
            middle = ( left + right ) // 2

            if nums[middle] == target:
                return middle

            if nums[left] <= nums[middle]:  # 左～真ん中まではソートされた状態
                if target < nums[left] or nums[middle] < target:    # 左部分にはターゲットがないとき
                    left = middle + 1
                else:
                    right = middle-1
            
            else: # nums[left] > nums[middle] 真ん中から右までソートされた状態のとき
                if target < nums[middle] or nums[right] < target:   # 右部分にターゲットがないとき
                    right = middle -1
                else:
                    left = middle + 1
        
        return -1
