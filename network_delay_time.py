# https://leetcode.com/problems/network-delay-time

import collections
import heapq
import sys
from typing import List


def dijkstra(n, graph, start):
    dist = {node: sys.maxsize for node in range(1, n + 1)}
    dist[start] = 0

    heap = [(distance, neighbour) for neighbour, distance in graph[start]]
    heapq.heapify(heap)

    while heap:
        distance, nxt = heapq.heappop(heap)
        if distance < dist[nxt]:
            dist[nxt] = distance
            for neighbour, d in graph[nxt]:
                heapq.heappush(heap, (distance + d, neighbour))
    return dist


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, time in times:
            graph[u].append((v, time))

        res = max(dijkstra(n, graph, k))
        return -1 if res == sys.maxsize else res


if __name__ == '__main__':
    print(Solution().networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))
    print(Solution().networkDelayTime(times=[[1, 2, 1]], n=2, k=1))
    print(Solution().networkDelayTime(times=[[1, 2, 1]], n=2, k=2))
    print(Solution().networkDelayTime([[1, 2, 1], [2, 3, 2], [1, 3, 4]], n=3, k=1))
    print(Solution().networkDelayTime([[1, 2, 1], [2, 1, 3]], 2, 2))
    print(Solution().networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
    print(Solution().networkDelayTime(
        [[4, 2, 76], [1, 3, 79], [3, 1, 81], [4, 3, 30], [2, 1, 47], [1, 5, 61], [1, 4, 99], [3, 4, 68], [3, 5, 46],
         [4, 1, 6], [5, 4, 7], [5, 3, 44], [4, 5, 19], [2, 3, 13], [3, 2, 18], [1, 2, 0], [5, 1, 25], [2, 5, 58],
         [2, 4, 77], [5, 2, 74]], 5, 3))

    print(Solution().networkDelayTime(
        [[2, 4, 10], [5, 2, 38], [3, 4, 33], [4, 2, 76], [3, 2, 64], [1, 5, 54], [1, 4, 98], [2, 3, 61], [2, 1, 0],
         [3, 5, 77], [5, 1, 34], [3, 1, 79], [5, 3, 2], [1, 2, 59], [4, 3, 46], [5, 4, 44], [2, 5, 89], [4, 5, 21],
         [1, 3, 86], [4, 1, 95]], 5, 1))

    print(Solution().networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
