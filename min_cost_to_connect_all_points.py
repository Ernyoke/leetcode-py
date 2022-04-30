# https://leetcode.com/problems/min-cost-to-connect-all-points

from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim's algorith
        if not points:
            return 0

        d = {(x, y): float('inf') for x, y in points}
        d[tuple(points[0])] = 0

        ans = 0
        while d:
            x, y = min(d, key=d.get)
            ans += d.pop((x, y))
            for x_2, y_2 in d.keys():
                d[(x_2, y_2)] = min(d[(x_2, y_2)], abs(x - x_2) + abs(y - y_2))

        return ans


if __name__ == '__main__':
    print(Solution().minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
