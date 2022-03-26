# https://leetcode.com/problems/binary-search/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            index = end - (end - start) // 2
            if target < nums[index]:
                end = index - 1
            else:
                start = index

        return start if nums[start] == target else -1


if __name__ == '__main__':
    print(Solution().search([-1, 0, 3, 5, 9, 12], 9))
    print(Solution().search([-1, 0, 3, 5, 9, 12], 2))
    print(Solution().search([5], 5))
    print(Solution().search([2, 5], 2))
