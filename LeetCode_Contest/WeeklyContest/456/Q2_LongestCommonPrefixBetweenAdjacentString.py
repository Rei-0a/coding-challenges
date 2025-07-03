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