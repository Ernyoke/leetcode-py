# https://leetcode.com/problems/sort-array-by-increasing-frequency/
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = {}
        for num in nums:
            d.setdefault(num, 0)
            d[num] += 1
        nums.sort(key=lambda v: (d[v], -v))
        return nums


if __name__ == '__main__':
    print(Solution().frequencySort([1, 1, 2, 2, 2, 3]))
    print(Solution().frequencySort([2, 3, 1, 3, 2]))
