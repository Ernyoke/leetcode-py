# https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number

from typing import List


class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        x, y, z = num // 3 - 1, num // 3, num // 3 + 1

        if x + y + z == num:
            return [x, y, z]
        return []


if __name__ == '__main__':
    print(Solution().sumOfThree(33))