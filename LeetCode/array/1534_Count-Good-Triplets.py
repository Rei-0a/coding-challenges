# Problem: https://leetcode.com/problems/count-good-triplets/description/
# Difficulty: Easy
# Date: 21/06/2025
'''
Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.

Return the number of good triplets.

'''

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