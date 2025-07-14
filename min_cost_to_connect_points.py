# https://neetcode.io/problems/min-cost-to-connect-points

import heapq
from collections import defaultdict
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i, [x1, y1] in enumerate(points):
            for j in range(i + 1):
                [x2, y2] = points[j]
                if i != j:
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    adj[i].append((j, dist))
                    adj[j].append((i, dist))

        return prim(adj)


def prim(adj: dict) -> int:
    heap = [(w, dest) for dest, w in adj[0]]
    heapq.heapify(heap)
    visited = set()
    visited.add(0)
    edges = []

    while heap:
        w, dest = heapq.heappop(heap)
        if dest not in visited:
            edges.append(w)
            visited.add(dest)
            for next_node, next_w in adj[dest]:
                heapq.heappush(heap, (next_w, next_node))

    return sum(edges)


if __name__ == '__main__':
    s = Solution()
    points = [[0, 0], [2, 2], [3, 3], [2, 4], [4, 2]]
    print(s.minCostConnectPoints(points))

    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    print(s.minCostConnectPoints(points))

    points = [[0, 0], [1, 1], [1, 0], [-1, 1]]
    print(s.minCostConnectPoints(points))
