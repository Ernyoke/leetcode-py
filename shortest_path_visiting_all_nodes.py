# https://leetcode.com/problems/shortest-path-visiting-all-node

from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if len(graph) <= 1:
            return 0

        final_state = 0
        for i in range(len(graph)):
            final_state |= 1 << i

        queue = [(node, 1 << node) for node in range(len(graph))]
        seen = set(queue)
        step = 0
        while queue:
            new_queue = []
            while queue:
                node, state = queue.pop()
                if state == final_state:
                    return step
                for neighbour in graph[node]:
                    new_state = state | (1 << neighbour)
                    if (neighbour, new_state) not in seen:
                        seen.add((neighbour, new_state))
                        new_queue.append((neighbour, new_state))
            step += 1
            queue = new_queue


if __name__ == '__main__':
    print(Solution().shortestPathLength([[1, 2, 3], [0], [0], [0]]))
    print(Solution().shortestPathLength([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]))
    print(Solution().shortestPathLength([[1], [0, 2, 4], [1, 3], [2], [1, 5], [4]]))
