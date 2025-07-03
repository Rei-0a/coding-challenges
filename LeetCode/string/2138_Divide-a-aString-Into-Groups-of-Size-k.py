# Problem: https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/
# Difficulty: Easy
# Date: 2025-06-22

class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """

        answers = []
        index = 0
        while index < len(s):
            ans = s[index:index+k]
            if index + k > len(s):
                ans += fill*(k - len(s)%k)
            index += k
            answers.append(ans)
        return answers