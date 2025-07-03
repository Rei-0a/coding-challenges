# Problem: https://leetcode.com/problems/longest-common-prefix/description/
# Difficulty: Easy
# Date: 2025-07-03

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        answer = ''
        min_len = len(strs[0])
        for word in strs:
            if len(word) < min_len:
                min_len = len(word)
        
        for index in range(min_len):
            letter = strs[0][index]
            for word in strs:
                if word[index] != letter:
                    return answer 
            answer += letter
        
        return answer