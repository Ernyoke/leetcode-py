# https://leetcode.com/problems/maximum-subarray/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        prev_max = nums[0]
        res = prev_max
        for i in range(1, len(nums)):
            prev_max = max(nums[i], prev_max + nums[i])
            res = max(res, prev_max)
        return res


if __name__ == "__main__":
    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))