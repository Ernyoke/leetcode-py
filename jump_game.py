# https://leetcode.com/problems/jump-game

from typing import List


class Solution:
    def canJump_slow(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True

        n = len(nums)
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, min(i + nums[i] + 1, n)):
                if dp[j]:
                    dp[i] = True
                    break

        return dp[0]

    def canJump(self, nums: List[int]) -> bool:
        index = len(nums) - 1

        n = len(nums)
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= index:
                index = i

        return index == 0


if __name__ == '__main__':
    print(Solution().canJump([2, 3, 1, 1, 4]))
    print(Solution().canJump([3, 2, 1, 0, 4]))
