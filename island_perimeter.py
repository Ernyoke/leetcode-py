# https://leetcode.com/problems/island-perimeter

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        touched = set()
        n = len(grid)
        m = len(grid[0])
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i, j) not in touched:
                    stack = [(i, j)]
                    touched.add((i, j))
                    while stack:
                        x, y = stack.pop()
                        for d_x, d_y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                            new_x, new_y = x + d_x, y + d_y
                            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
                                count += 1
                                continue
                            if 0 <= new_x < n and 0 <= new_y < m:
                                if grid[new_x][new_y] == 0:
                                    count += 1
                                    continue
                                if (new_x, new_y) not in touched:
                                    stack.append((new_x, new_y))
                                    touched.add((new_x, new_y))
        return count


if __name__ == '__main__':
    print(Solution().islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
