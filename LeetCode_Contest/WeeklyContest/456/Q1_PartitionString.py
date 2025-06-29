'''
LeetCode_Contest/WeeklyContest/456/Q1_PartitionString.py
Medium

29/06/25

Given a string s, partition it into unique segments according to the following procedure:

Start building a segment beginning at index 0.
Continue extending the current segment character by character until the current segment has not been seen before.
Once the segment is unique, add it to your list of segments, mark it as seen, and begin a new segment from the next index.
Repeat until you reach the end of s.
Return an array of strings segments, where segments[i] is the ith segment created.

'''

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