# https://leetcode.com/problems/first-missing-positive/
import sys
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            nums[i] = num if num > 0 else 0

        for i, num in enumerate(nums):
            index = abs(num) - 1
            if 0 <= index < len(nums):
                if nums[index] == 0:
                    nums[index] = -sys.maxsize
                elif nums[index] > 0:
                    nums[index] *= -1

        for index, num in enumerate(nums):
            if num >= 0:
                return index + 1

        return len(nums) + 1


if __name__ == '__main__':
    print(Solution().firstMissingPositive([3, 4, -1, 1]))
    print(Solution().firstMissingPositive([1]))
    print(Solution().firstMissingPositive([2, 1]))
    print(Solution().firstMissingPositive([7, 8, 9, 11, 12]))
