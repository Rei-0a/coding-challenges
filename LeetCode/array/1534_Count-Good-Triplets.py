# Problem: https://leetcode.com/problems/count-good-triplets/description/
# Difficulty: Easy
# Date: 2025-06-21

class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int] 3,0,1,1,9,7
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        goodTriplets = 0

        for i in range(len(arr)-2):
            for j in range(i+1,len(arr)-1):
                for k in range(j+1,len(arr)):
                    isGoodtriplets = True
                    if abs(arr[i]-arr[j]) <= a and abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                        goodTriplets += 1

        return goodTriplets