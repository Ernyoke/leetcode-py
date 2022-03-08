# https://leetcode.com/problems/permutations

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        stack = [{num: 0} for num in nums]

        ans = []
        while stack:
            current = stack.pop()
            for num in nums:
                if len(nums) == len(current):
                    ans.append(current)
                    break
                elif num not in current:
                    nxt = dict(current)
                    nxt[num] = 0
                    stack.append(nxt)
        return [list(d.keys()) for d in ans]


if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))
