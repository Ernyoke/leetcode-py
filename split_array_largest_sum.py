# https://leetcode.com/problems/split-array-largest-sum

from typing import List


class Solution:
    @staticmethod
    def get_possible_splits(nums, target):
        count, current_sum = 0, 0
        for num in nums:
            current_sum += num
            if current_sum > target:
                count += 1
                current_sum = num

        return count + 1

    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums), sum(nums)
        ans = (left + right) // 2
        while left <= right:
            mid = (left + right) // 2
            if Solution.get_possible_splits(nums, mid) <= m:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans


if __name__ == '__main__':
    print(Solution().splitArray([7, 2, 5, 10, 8], 2))
    print(Solution().splitArray([1, 2, 3, 4, 5], 2))
