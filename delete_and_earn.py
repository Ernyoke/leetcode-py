# https://leetcode.com/problems/delete-and-earn/submissions/

from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # Transform this problem into house_robber problem
        points = [0] * (max(nums) + 1)
        for num in nums:
            points[num] += num

        return self.rob(points[1:])

    def rob(self, nums: List[int]) -> int:
        prev_robbed = 0
        prev_not_robbed = 0
        for index, num in enumerate(nums):
            aux = prev_not_robbed
            prev_not_robbed = max(prev_robbed, prev_not_robbed)
            prev_robbed = num + aux

        return max(prev_robbed, prev_not_robbed)


if __name__ == '__main__':
    print(Solution().deleteAndEarn([2, 2, 3, 3, 3, 4]))
    print(Solution().deleteAndEarn([3, 4, 2]))
