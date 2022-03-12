# https://leetcode.com/problems/next-permutation
# https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        k = n - 2
        while k >= 0:
            if nums[k] < nums[k + 1]:
                break
            k -= 1

        if k == -1:
            nums.reverse()
            return

        l = n - 1
        while l > k:
            if nums[k] < nums[l]:
                break
            l -= 1

        nums[k], nums[l] = nums[l], nums[k]

        for i in range(k + 1, k + 1 + (n - k - 1) // 2):
            nums[i], nums[n - i + k] = nums[n - i + k], nums[i]


if __name__ == '__main__':
    lst = [1, 2, 3]
    Solution().nextPermutation(lst)
    print(lst)

    lst = [3, 2, 1]
    Solution().nextPermutation(lst)
    print(lst)

    lst = [1, 1, 5]
    Solution().nextPermutation(lst)
    print(lst)

    lst = [2, 3, 1]
    Solution().nextPermutation(lst)
    print(lst)

    lst = [1, 3, 2]
    Solution().nextPermutation(lst)
    print(lst)

    lst = [5, 4, 7, 5, 3, 2]
    Solution().nextPermutation(lst)
    print(lst)

    lst = [4, 2, 0, 3, 2, 2, 0]
    Solution().nextPermutation(lst)
    print(lst)
