# https://leetcode.com/problems/count-good-triplets-in-an-array/

from typing import List
from sortedcontainers import SortedList


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        pos = [0] * len(nums2)
        for i, num in enumerate(nums2):
            pos[num] = i

        sorted_list = SortedList()
        prefix = []
        for num in nums1:
            position = pos[num]
            prefix.append(sorted_list.bisect(position))
            sorted_list.add(position)

        sorted_list.clear()
        suffix = []
        for num in nums1[::-1]:
            position = pos[num]
            suffix.append(len(sorted_list) - sorted_list.bisect(position))
            sorted_list.add(position)

        suffix.reverse()
        ans = 0
        for i in range(0, len(nums1)):
            ans += prefix[i] * suffix[i]

        return ans


if __name__ == "__main__":
    print(Solution().goodTriplets([2, 0, 1, 3], [0, 1, 2, 3]))
    nums1 = [4, 0, 1, 3, 2]
    nums2 = [4, 1, 0, 2, 3]
    print(Solution().goodTriplets(nums1, nums2))
