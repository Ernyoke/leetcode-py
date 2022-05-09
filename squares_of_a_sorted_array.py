# https://leetcode.com/problems/squares-of-a-sorted-array/

from typing import List


class Solution:
    def sortedSquares_slow(self, nums: List[int]) -> List[int]:
        return list(sorted(map(lambda x: x ** 2, nums)))

    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        res = []
        while i <= j:
            a = nums[i] ** 2
            b = nums[j] ** 2
            if a > b:
                res.append(a)
                i += 1
            else:
                res.append(b)
                j -= 1
        return res[::-1]


if __name__ == '__main__':
    print(Solution().sortedSquares([-4, -1, 0, 3, 10]))
