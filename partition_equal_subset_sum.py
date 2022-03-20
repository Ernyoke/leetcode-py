# https://leetcode.com/problems/partition-equal-subset-sum/

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 > 0:
            return False

        part = sum_nums // 2

        if max(nums) > part:
            return False

        dp = [False] * (part + 1)

        dp[0] = True

        for num in nums:
            for i in range(part, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[part]


if __name__ == '__main__':
    print(Solution().canPartition([1, 5, 11, 5]))
    print(Solution().canPartition([1, 2, 3, 5]))
    print(Solution().canPartition([2, 4, 10, 18]))
    print(Solution().canPartition([1, 3, 0, 4]))
