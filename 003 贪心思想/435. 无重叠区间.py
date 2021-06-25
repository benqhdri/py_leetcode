from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0], reverse=True)
        intervals.sort(key=lambda x: x[1])

        ans = 0
        j = 1
        while j < len(intervals):
            if intervals[j][0] < intervals[j - 1][1]:
                # 如果有重叠
                intervals.pop(j)
                ans += 1
            else:
                j += 1

        return ans
