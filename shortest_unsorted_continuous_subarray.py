# https://leetcode.com/problems/shortest-unsorted-continuous-subarray

from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        end, max_value = -2, nums[0]
        for i, num in enumerate(nums[1:]):
            max_value = max(max_value, num)
            if num < max_value:
                end = i + 1

        start, min_value = -1, nums[-1]
        for i, num in enumerate(nums[::-1]):
            min_value = min(min_value, num)
            if num > min_value:
                start = len(nums) - i - 1

        return end - start + 1


if __name__ == '__main__':
    print(Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
    print(Solution().findUnsortedSubarray([1, 2, 3, 4]))
