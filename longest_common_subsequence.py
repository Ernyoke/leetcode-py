# https://leetcode.com/problems/longest-common-subsequence/submissions/

import functools
import sys

sys.setrecursionlimit(10 ** 9)


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1)]
        for _ in text1:
            dp.append([0] * (len(text2) + 1))

        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[len(text1)][len(text2)]

    def longestCommonSubsequence_slow(self, text1: str, text2: str) -> int:

        @functools.lru_cache(maxsize=None)
        def compute(part1, part2):
            if len(part1) == 0 or len(part2) == 0:
                return 0
            if part1[-1] == part2[-1]:
                return 1 + compute(part1[:-1], part2[:-1])
            else:
                return max(compute(part1, part2[:-1]), compute(part1[:-1], part2))

        return compute(text1, text2)


if __name__ == '__main__':
    print(Solution().longestCommonSubsequence('abcde', 'ace'))
    print(Solution().longestCommonSubsequence_slow('abcde', 'ace'))
