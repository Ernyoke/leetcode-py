# https://leetcode.com/problems/ones-and-zeroes

import functools
import sys
from typing import List


def count_digits(str):
    zero, one = 0, 0
    for char in str:
        if char == '0':
            zero += 1
        elif char == '1':
            one += 1

    return zero, one


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        c = [count_digits(s) for s in strs]

        for zero, one in c:
            for i in range(m, zero - 1, -1):
                for j in range(n, one - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - zero][j - one])

        return dp[m][n]

    def findMaxFormRecursive(self, strs: List[str], m: int, n: int) -> int:
        c = [count_digits(s) for s in strs]

        @functools.cache
        def rec(zeros, ones, index):
            if zeros < 0 or ones < 0:
                return -(sys.maxsize - 1)

            if index >= len(strs):
                return 0

            zero, one = c[index]
            return max(rec(zeros, ones, index + 1), 1 + rec(zeros - zero, ones - one, index + 1))

        return rec(m, n, 0)


if __name__ == '__main__':
    print(Solution().findMaxForm(strs=["10", "0001", "111001", "1", "0"], m=5, n=3))
    print(Solution().findMaxForm(strs=["10", "0", "1"], m=1, n=1))

    print(Solution().findMaxFormRecursive(strs=["10", "0001", "111001", "1", "0"], m=5, n=3))
    print(Solution().findMaxFormRecursive(strs=["10", "0", "1"], m=1, n=1))
    print(Solution().findMaxFormRecursive(["00", "000"], 1, 10))
    print(Solution().findMaxFormRecursive(["10", "0001", "111001", "1", "0"], 3, 4))
