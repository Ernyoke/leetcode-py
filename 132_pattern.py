# https://leetcode.com/problems/132-pattern

import sys
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        s3 = -(sys.maxsize - 1)
        for num in nums[::-1]:
            if num < s3:
                return True
            while stack and stack[-1] < num:
                s3 = stack.pop()

            stack.append(num)

        return False


if __name__ == '__main__':
    print(Solution().find132pattern([1, 2, 3, 4]))
    print(Solution().find132pattern([3, 1, 4, 2]))
    print(Solution().find132pattern([-1, 3, 2, 0]))
    print(Solution().find132pattern([1, 0, 1, -4, -3]))
    print(Solution().find132pattern([-2, 1, -2]))
    print(Solution().find132pattern([1, 3, 2, 4, 5, 6, 7, 8, 9, 10]))
    print(Solution().find132pattern([-2, 1, 1]))
