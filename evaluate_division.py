# https://leetcode.com/problems/evaluate-division

import collections
from typing import List


def floyd_warshall(g: collections.defaultdict[list]):
    dist = []
    for i in range(len(g)):
        dist.append([float('inf')] * len(g))
    for i in range(len(g)):
        dist[i][i] = 1.0
    index_map = {index: value for value, index in enumerate(g.keys())}
    for node_1, nodes in g.items():
        for node_2, edge in nodes:
            x, y = index_map[node_1], index_map[node_2]
            dist[x][y] = edge

    for k in range(len(dist)):
        for i in range(len(dist)):
            for j in range(len(dist)):
                if dist[i][j] > dist[i][k] * dist[k][j]:
                    dist[i][j] = dist[i][k] * dist[k][j]

    return index_map, dist


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = collections.defaultdict(list)
        for i in range(len(equations)):
            g[equations[i][0]].append((equations[i][1], values[i]))
            g[equations[i][1]].append((equations[i][0], 1 / values[i]))

        index_map, dist = floyd_warshall(g)
        ans = []
        for a, b in queries:
            if a in index_map and b in index_map:
                answer = dist[index_map[a]][index_map[b]]
                ans.append(answer if answer != float('inf') else -1.0)
            else:
                ans.append(-1.0)

        return ans


if __name__ == '__main__':
    print(Solution().calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0],
                                  [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))

    print(Solution().calcEquation([["a", "b"]], [0.5],
                                  [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]))

    print(Solution().calcEquation([["a", "b"], ["c", "d"]], [1.0, 1.0],
                                  [["a", "c"], ["b", "d"], ["b", "a"], ["d", "c"]]))
