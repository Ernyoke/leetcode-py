# https://leetcode.com/problems/permutations-ii

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        stack = [(i,) for i, num in enumerate(nums)]

        ans = set()
        while stack:
            current = stack.pop()
            for i, num in enumerate(nums):
                if len(nums) == len(current):
                    ans.add(tuple([nums[i] for i in current]))
                    break
                elif i not in current:
                    stack.append((*current, i))
        return [list(d) for d in ans]


if __name__ == '__main__':
    print(Solution().permuteUnique([1, 1, 2]))
