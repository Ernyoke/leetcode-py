# https://leetcode.com/problems/two-sum

from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(list)
        for index, num in enumerate(nums):
            d[num].append(index)

        for index, num in enumerate(nums):
            if target - num in d:
                pos = d[target - num]
                for p in pos:
                    if p != index:
                        return [index, p]

        return []


if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
