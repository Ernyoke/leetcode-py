# https://leetcode.com/problems/shift-2d-grid/

from typing import List


def rotate(l, n):
    return l[-n:] + l[:-n]


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        prev = []
        for i in range(n):
            prev.append(grid[i][0])
        for shift in range(k):
            for j in range(1, m):
                aux = []
                for i in range(n):
                    aux.append(grid[i][j])
                    grid[i][j] = prev[i]
                prev = aux

            prev = rotate(prev, 1)
            for i in range(n):
                grid[i][0] = prev[i]

        return grid


if __name__ == '__main__':
    print(Solution().shiftGrid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))
    print(Solution().shiftGrid([[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], 4))
