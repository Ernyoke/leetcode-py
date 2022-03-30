# https://leetcode.com/problems/find-the-duplicate-number/

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 1, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            cnt = len([1 for num in nums if num <= mid])

            if cnt <= mid:
                low = mid + 1
            else:
                high = mid - 1

        return low


if __name__ == '__main__':
    print(Solution().findDuplicate([1, 3, 4, 2, 2]))
    print(Solution().findDuplicate([9, 4, 9, 5, 7, 2, 8, 9, 3, 9]))
