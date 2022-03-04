# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/

from collections import defaultdict
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        d = dict((i, defaultdict(int)) for i in range(n))

        i = 1
        ans = 0
        while i < n:
            for j in range(i - 1, -1, -1):
                diff = nums[i] - nums[j]
                cnt = d[j][diff] if diff in d[j] else 0
                d[i][diff] += cnt + 1
                ans += cnt
            i += 1

        print(d)
        return ans


if __name__ == '__main__':
    print(Solution().numberOfArithmeticSlices([2, 4, 6, 8, 10]))
    print(Solution().numberOfArithmeticSlices([7, 7, 7, 7, 7]))
    print(Solution().numberOfArithmeticSlices([79, 20, 64, 28, 67, 81, 60, 58, 97, 85, 92, 96, 82, 89, 46, 50, 15, 2,
                                               36, 44, 54, 2, 90, 37, 7, 79, 26, 40, 34, 67, 64, 28, 60, 89, 46, 31, 9,
                                               95, 43, 19, 47, 64, 48, 95, 80, 31, 47, 19, 72, 99, 28, 46, 13, 9, 64,
                                               4, 68, 74, 50, 28, 69, 94, 93, 3, 80, 78, 23, 80, 43, 49, 77, 18, 68,
                                               28, 13, 61, 34, 44, 80, 70, 55, 85, 0, 37, 93, 40, 47, 47, 45, 23, 26,
                                               74, 45, 67, 34, 20, 33, 71, 48, 96]))
