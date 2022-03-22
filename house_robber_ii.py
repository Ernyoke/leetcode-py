# https://leetcode.com/problems/house-robber-ii

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self._rob(nums[:-1]), self._rob(nums[1:]))

    @staticmethod
    def _rob(nums: List[int]) -> int:
        prev_robbed = 0
        prev_not_robbed = 0
        for num in nums:
            aux = prev_not_robbed
            prev_not_robbed = max(prev_robbed, prev_not_robbed)
            prev_robbed = num + aux

        return max(prev_robbed, prev_not_robbed)


if __name__ == "__main__":
    print(Solution().rob([2, 3, 2]))
    print(Solution().rob([1, 2, 3, 1]))
    print(Solution().rob([1, 2, 3]))
    print(Solution().rob([1]))
