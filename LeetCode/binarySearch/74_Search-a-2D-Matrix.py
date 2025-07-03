# Problem: https://leetcode.com/problems/search-a-2d-matrix/
# Difficulty: Medium
# Date: 2025-06-25

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]   # m * n matrix
        :type target: int
        :rtype: bool
        """
        m = len(matrix) #m行
        n = len(matrix[0])  #n列

        # 何行目かを探す
        up = 0
        down = m - 1
        while up <= down:
            line_mid = ( up + down ) // 2
            if matrix[line_mid][0] == target:
                return True
            elif matrix[line_mid][0] < target <= matrix[line_mid][n-1]:
                break
            
            if target < matrix[line_mid][0]:
                down = line_mid - 1
            elif matrix[line_mid][0] < target:
                up = line_mid + 1
        
        # 何列目かを探す
        left = 0
        right = n - 1
        
        while left <= right:
            row_mid = ( left + right ) // 2
            if matrix[line_mid][row_mid] == target:
                return True
            elif matrix[line_mid][row_mid] < target:
                left = row_mid + 1
            else:   # target < matrix[line_mid][row_mid]
                right = row_mid - 1
        
        return False
            
