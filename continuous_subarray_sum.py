# https://leetcode.com/problems/continuous-subarray-sum

from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mods = {0: -1}
        running_sum = 0
        for i, num in enumerate(nums):
            running_sum += num
            running_sum %= k
            if running_sum in mods:
                if i - mods[running_sum] > 1:
                    return True
            else:
                mods[running_sum] = i

        return False


if __name__ == '__main__':
    print(Solution().checkSubarraySum([23, 2, 4, 6, 7], 6))
    print(Solution().checkSubarraySum([23, 2, 6, 4, 7], 6))
    print(Solution().checkSubarraySum([23, 2, 6, 4, 7], 13))
    print(Solution().checkSubarraySum([23, 2, 4, 6, 6], 7))
    print(Solution().checkSubarraySum([5, 0, 0, 0], 3))
    print(Solution().checkSubarraySum([2, 4, 3], 6))
    print(Solution().checkSubarraySum([1, 0], 2))
