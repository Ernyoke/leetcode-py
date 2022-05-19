# https://leetcode.com/problems/longest-increasing-path-in-a-matrix

from typing import List


class Solution:
    def __init__(self):
        self.dp = []
        for i in range(0, 200):
            self.dp.append([0] * 200)

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ans = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                ans = max(ans, self.solve(matrix, i, j, -1))
        return ans

    def solve(self, matrix, i, j, prev):
        if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and matrix[i][j] > prev:
            if self.dp[i][j]:
                return self.dp[i][j]
            self.dp[i][j] = 1 + max([self.solve(matrix, i - 1, j, matrix[i][j]),
                                     self.solve(matrix, i + 1, j, matrix[i][j]),
                                     self.solve(matrix, i, j - 1, matrix[i][j]),
                                     self.solve(matrix, i, j + 1, matrix[i][j])])
            return self.dp[i][j]
        return 0


if __name__ == '__main__':
    print(Solution().longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
    print(Solution().longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]))
