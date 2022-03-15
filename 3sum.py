# https://leetcode.com/problems/3sum

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i, target in enumerate(nums):
            if i > 0 and target == nums[i - 1]:
                continue
            start, end = i + 1, len(nums) - 1
            while start < end:
                if nums[start] + nums[end] == -target:
                    ans.append([target, nums[start], nums[end]])
                    start += 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                elif nums[start] + nums[end] < -target:
                    start += 1
                else:
                    end -= 1
        return ans


if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
    print(Solution().threeSum([]))
    print(Solution().threeSum([0]))
