# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero

from typing import List
import sys


class Solution:
    # DP, does not pass all the tests
    def minOperations_slow(self, nums: List[int], x: int) -> int:
        cache = {}

        def compute_operations(numbers, current, steps):
            t = tuple(numbers)
            if (t, current) in cache:
                return cache[(t, current)]
            if current == 0:
                cache[(t, current)] = steps
                return steps
            if current < 0:
                cache[(t, current)] = sys.maxsize
                return sys.maxsize
            if len(numbers) <= 0:
                return sys.maxsize
            a = compute_operations(numbers[1:], current - numbers[0], steps + 1)
            b = compute_operations(numbers[:-1], current - numbers[-1], steps + 1)
            return min(a, b)

        res = compute_operations(nums, x, 0)
        return -1 if res == sys.maxsize else res

    def minOperations(self, nums: List[int], x: int) -> int:
        s = sum(nums)
        max_length = -1
        curr_sum = 0

        left, right = 0, 0
        while right < len(nums):
            curr_sum += nums[right]

            while left <= right and curr_sum > s - x:
                curr_sum -= nums[left]
                left += 1

            if curr_sum == s - x:
                max_length = max(max_length, right - left + 1)
            right += 1

        return -1 if max_length == -1 else len(nums) - max_length


if __name__ == '__main__':
    print(Solution().minOperations(nums=[1, 1, 4, 2, 3], x=5))
    print(Solution().minOperations(nums=[5, 6, 7, 8, 9], x=4))
    print(Solution().minOperations(nums=[3, 2, 20, 1, 1, 3], x=10))
    print(Solution().minOperations(nums=[1, 1], x=3))
    print(Solution().minOperations(
        [6016, 5483, 541, 4325, 8149, 3515, 7865, 2209, 9623, 9763, 4052, 6540, 2123, 2074, 765, 7520, 4941, 5290, 5868,
         6150, 6006, 6077, 2856, 7826, 9119], 31841))
    print(Solution().minOperations(
        [1241, 8769, 9151, 3211, 2314, 8007, 3713, 5835, 2176, 8227, 5251, 9229, 904, 1899, 5513, 7878, 8663, 3804,
         2685, 3501, 1204, 9742, 2578, 8849, 1120, 4687, 5902, 9929, 6769, 8171, 5150, 1343, 9619, 3973, 3273, 6427,
         47, 8701, 2741, 7402, 1412, 2223, 8152, 805, 6726, 9128, 2794, 7137, 6725, 4279, 7200, 5582, 9583, 7443,
         6573, 7221, 1423, 4859, 2608, 3772, 7437, 2581, 975, 3893, 9172, 3, 3113, 2978, 9300, 6029, 4958, 229, 4630,
         653, 1421, 5512, 5392, 7287, 8643, 4495, 2640, 8047, 7268, 3878, 6010, 8070, 7560, 8931, 76, 6502, 5952,
         4871, 5986, 4935, 3015, 8263, 7497, 8153, 384, 1136], 894887480))
