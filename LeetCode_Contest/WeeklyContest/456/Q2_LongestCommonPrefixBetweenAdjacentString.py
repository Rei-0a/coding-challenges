'''
You are given an array of strings words. For each index i in the range [0, words.length - 1], perform the following steps:

Remove the element at index i from the words array.
Compute the length of the longest common prefix among all adjacent pairs in the modified array.
Return an array answer, where answer[i] is the length of the longest common prefix between the adjacent pairs after removing the element at index i. If no adjacent pairs remain or if none share a common prefix, then answer[i] should be 0.

A prefix of a string is a substring that starts from the beginning of the string and extends to any point within it.
 
 
'''

'''
Time Limit Exceeded
'''

import numpy as np
class Solution(object):
    def longestCommonPrefix(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """

        def count_longestcommonprefix(words):
            max = 0
            for i in range(len(words)-1):
                count = 0
                while count < min(len(words[i]),len(words[i+1])) and words[i][count] == words[i+1][count]:
                    count += 1

                if max < count:
                    max = count

            return max

        remove_index = 0
        while remove_index < len(words):
            words_without_remove = words[:remove_index]+words[remove_index+1:]
            value = count_longestcommonprefix(words_without_remove)
            remove_index += 1