# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

import bisect
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        index = bisect.bisect_left(nums, target)
        if index < len(nums) and nums[index] == target:
            start = end = index
            for i in range(index - 1, -1, -1):
                if nums[i] != target:
                    break
                start = i
            for i in range(index + 1, len(nums)):
                if nums[i] != target:
                    break
                end = i
            return [start, end]
        else:
            return [-1, -1]


if __name__ == '__main__':
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
