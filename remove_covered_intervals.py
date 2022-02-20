# https://leetcode.com/problems/remove-covered-intervals/submissions/

from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: (interval[0], -interval[1]))
        removed = 0
        i = 0
        while i < len(intervals):
            current = intervals[i]
            j = i + 1
            while j < len(intervals):
                nxt = intervals[j]
                if nxt[1] <= current[1]:
                    removed += 1
                    j += 1
                else:
                    break
            i = j
        return len(intervals) - removed


if __name__ == '__main__':
    print(Solution().removeCoveredIntervals([[1, 4], [3, 6], [2, 8]]))
    print(Solution().removeCoveredIntervals([[1, 4], [2, 3]]))
    print(Solution().removeCoveredIntervals([[1, 2], [1, 4], [3, 4]]))
