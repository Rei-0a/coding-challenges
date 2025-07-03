'''
LeetCode_Contest/WeeklyContest/456/Q1_PartitionString.py
Medium

29/06/25
'''

# Problem: url
# Difficulty: Medium
# Date : 2025-06-29

class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        segments = set()
        answer = []
        index = 0
        
        while index < len(s): # index = 2 < 8
            if not(s[index] in segments):  # 新しい文字だったとき
                segments.add(s[index])
                answer.append(s[index])

            else:
                SeenSegments = True
                key = s[index] # key = b
                while SeenSegments and index < len(s):# 新しくsegmentsに入ることのできる文字が見つかるまで次の文字を探す
                    index += 1 # index = 3
                    if index == len(s):
                        break
                    key += s[index]
                    if not(key in segments):  # もし新しくsegmentsに入ることができるなら、このループを抜ける
                        segments.add(key)
                        answer.append(key)
                        SeenSegments = False
            index += 1
            
        return answer