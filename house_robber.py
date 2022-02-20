# https://leetcode.com/problems/house-robber/

import functools
import sys
from typing import List

sys.setrecursionlimit(10 ** 9)


class Solution:
    def rob_slow(self, nums: List[int]) -> int:

        @functools.lru_cache(maxsize=None)
        def rob_rec(ns):
            if not ns:
                return 0
            if len(ns) == 1:
                return ns[0]

            return max(ns[0] + rob_rec(ns[2:]), rob_rec(ns[1:]))

        return rob_rec(tuple(nums))

    def rob(self, nums: List[int]) -> int:
        prev_robbed = 0
        prev_not_robbed = 0
        for num in nums:
            aux = prev_not_robbed
            prev_not_robbed = max(prev_robbed, prev_not_robbed)
            prev_robbed = num + aux

        return max(prev_robbed, prev_not_robbed)


if __name__ == "__main__":
    print(Solution().rob([2, 7, 9, 3, 1]))
    # print(Solution().rob([1, 2, 3, 1]))
