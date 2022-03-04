# https://leetcode.com/problems/jump-game-ii/

import sys
from typing import List


class Solution:
    def jump_slow(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        i = len(nums) - 2
        while i >= 0:
            min_jmp = sys.maxsize
            for j in range(i + 1, min(i + 1 + nums[i], len(nums))):
                min_jmp = min(min_jmp, 1 + dp[j])
            dp[i] = min_jmp
            i -= 1
        print(dp)
        return dp[0]

    def jump(self, nums: List[int]) -> int:
        jumps = end = farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == end:
                jumps += 1
                end = farthest
        return jumps


if __name__ == '__main__':
    print(Solution().jump([2, 3, 1, 1, 4]))
    print(Solution().jump([2, 3, 0, 1, 4]))
