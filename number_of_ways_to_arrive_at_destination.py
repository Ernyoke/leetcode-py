# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination

import heapq
from collections import defaultdict
from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        if not roads:
            return 1

        adj = defaultdict(list)
        for road in roads:
            s, dest, w = road
            adj[s].append((dest, w))
            adj[dest].append((s, w))

        MOD = 10 ** 9 + 7
        heap = [(0,0)]
        min_cost = [float("inf")] * len(adj.keys())
        min_cost[0] = 0
        count_ways = [0] * len(adj.keys())
        count_ways[0] = 1

        while heap:
            cost, source = heapq.heappop(heap)
            for dest, w in adj[source]:
                if min_cost[dest] > cost + w:
                    heapq.heappush(heap, (cost + w, dest))
                    min_cost[dest] = cost + w
                    count_ways[dest] = count_ways[source]
                elif min_cost[dest] == cost + w:
                    count_ways[dest] = (count_ways[source] + count_ways[dest]) % MOD

        return count_ways[n - 1]


if __name__ == '__main__':
    s = Solution()
    roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5],
             [4, 6, 2]]
    print(s.countPaths(7, roads))
