# https://leetcode.com/problems/peak-index-in-a-mountain-array

from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low, high = 0, len(arr) - 1
        while low < high:
            mid = low + (high - low) // 2
            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid
        return low


if __name__ == '__main__':
    print(Solution().peakIndexInMountainArray([0, 2, 1, 0]))
    print(Solution().peakIndexInMountainArray([0, 1, 0]))
