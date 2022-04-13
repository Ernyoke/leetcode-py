# https://leetcode.com/problems/spiral-matrix-ii

from pprint import pprint
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        i, j = 0, 0
        k = 1
        for _ in range(n):
            while j < n and ans[i][j] == 0:
                ans[i][j] = k
                j += 1
                k += 1

            j -= 1
            i += 1
            while i < n and ans[i][j] == 0:
                ans[i][j] = k
                i += 1
                k += 1

            i -= 1
            j -= 1
            while j >= 0 and ans[i][j] == 0:
                ans[i][j] = k
                j -= 1
                k += 1

            i -= 1
            j += 1
            while i >= 0 and ans[i][j] == 0:
                ans[i][j] = k
                i -= 1
                k += 1

            i += 1
            j += 1

        return ans


if __name__ == '__main__':
    pprint(Solution().generateMatrix(3))
    pprint(Solution().generateMatrix(4))
    pprint(Solution().generateMatrix(1))
