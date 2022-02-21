# https://leetcode.com/problems/maximum-ascending-subarray-sum/
from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        prev = nums[0]
        s = prev
        ans = s
        for i in range(1, len(nums)):
            num = nums[i]
            if prev < num:
                s += num
            else:
                ans = max(s, ans)
                s = num
            prev = num
        return max(ans, s)


if __name__ == '__main__':
    print(Solution().maxAscendingSum([10, 20, 30, 5, 10, 50]))
    print(Solution().maxAscendingSum([10, 20, 30, 40, 50]))
    print(Solution().maxAscendingSum([12, 17, 15, 13, 10, 11, 12]))
    print(Solution().maxAscendingSum([3, 6, 10, 1, 8, 9, 9, 8, 9]))
