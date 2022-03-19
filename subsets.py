# https://leetcode.com/problems/subsets

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(current, i):
            ans.append(current[:])
            for j in range(i, len(nums)):
                current.append(nums[j])
                backtrack(current, j + 1)
                current.pop()

        backtrack([], 0)
        return ans


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))
    print(Solution().subsets([0]))
