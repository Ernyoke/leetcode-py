# https://leetcode.com/problems/combination-sum-iii

from copy import copy
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def rec(i, current_n, current_ans):
            if i == k + 1 and current_n == 0:
                ans.append(copy(current_ans))
            else:
                for num in range(i, 10):
                    if current_n - num >= 0 and num not in current_ans:
                        current_ans.append(num)
                        rec(i + 1, current_n - num, current_ans)
                        current_ans.pop()
                    else:
                        break

        rec(1, n, [])
        return ans


if __name__ == '__main__':
    print(Solution().combinationSum3(3, 9))
