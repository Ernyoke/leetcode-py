# https://leetcode.com/problems/rotate-image

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n // 2):
            for j in range(m):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        for i in range(n):
            for j in range(i + 1, m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == '__main__':
    x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(x)
    print(x)
