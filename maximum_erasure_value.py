from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        d = {}
        max_sum = current_sum = start_poz = 0
        for i, num in enumerate(nums):
            if num not in d:
                current_sum += num
            else:
                max_sum = max(max_sum, current_sum)
                for j in range(start_poz, d[num]):
                    current_sum -= nums[j]
                    del d[nums[j]]
                    start_poz += 1
                start_poz += 1
            d[num] = i

        return max(max_sum, current_sum)


if __name__ == '__main__':
    print(Solution().maximumUniqueSubarray(nums=[4, 2, 4, 5, 6]))
    print(Solution().maximumUniqueSubarray(nums=[5, 2, 1, 2, 5, 2, 1, 2, 5]))
    print(Solution().maximumUniqueSubarray(
        nums=[187, 470, 25, 436, 538, 809, 441, 167, 477, 110, 275, 133, 666, 345, 411, 459, 490, 266, 987, 965, 429,
              166, 809, 340, 467, 318, 125, 165, 809, 610, 31, 585, 970, 306, 42, 189, 169, 743, 78, 810, 70, 382, 367,
              490, 787, 670, 476, 278, 775, 673, 299, 19, 893, 817, 971, 458, 409, 886, 434]))
