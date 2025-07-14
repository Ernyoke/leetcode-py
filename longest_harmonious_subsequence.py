# https://leetcode.com/problems/longest-harmonious-subsequence

from collections import Counter
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        sorted_keys = sorted(counter)

        max_len = 0
        for i in range(len(sorted_keys) - 1):
            a, b = sorted_keys[i], sorted_keys[i + 1]
            if abs(a - b) == 1:
                max_len = max(max_len, counter[a] + counter[b])

        return max_len


if __name__ == '__main__':
    s = Solution()
    print(s.findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
    print(s.findLHS([1, 2, 3, 4]))
    print(s.findLHS([1, 1, 1, 1]))
