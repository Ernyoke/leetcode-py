# https://leetcode.com/problems/arithmetic-slices

from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        i = 1
        current_len = 0
        cnt = 0
        while i < len(nums) - 1:
            if nums[i] - nums[i - 1] == nums[i + 1] - nums[i]:
                current_len += 1
            else:
                current_len = 0
            cnt += current_len
            i += 1

        return cnt


if __name__ == '__main__':
    print(Solution().numberOfArithmeticSlices([1, 2, 3, 4, 5]))
    print(Solution().numberOfArithmeticSlices([1]))
