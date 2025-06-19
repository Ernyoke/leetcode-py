# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k

from typing import List, Counter


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window = Counter()
        current_sum = 0
        max_sum = 0

        for i in range(len(nums)):
            current_sum += nums[i]
            window[nums[i]] += 1

            if i - k >= 0:
                window[nums[i - k]] -= 1
                current_sum -= nums[i - k]
                if window[nums[i - k]] == 0:
                    del window[nums[i - k]]

            if len(window.keys()) == k:
                max_sum = max(max_sum, current_sum)

        return max_sum


if __name__ == '__main__':
    s = Solution()
    print(s.maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3))
    print(s.maximumSubarraySum([4,4,4], 3))
