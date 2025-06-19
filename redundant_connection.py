# https://leetcode.com/problems/redundant-connection

from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        u = UnionFind(len(edges) + 1)
        for [a, b] in edges:
            if not u.union(a, b):
                return [a, b]

        return []


class UnionFind(object):
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, current):
        if self.parent[current] != current:
            return self.find(self.parent[current])

        return current

    def union(self, a, b):
        parent_a, parent_b = self.find(a), self.find(b)
        if parent_a == parent_b:
            return False

        if self.rank[parent_a] > self.rank[parent_b]:
            self.parent[parent_b] = parent_a
            self.rank[parent_a] += self.rank[parent_b]
        else:
            self.parent[parent_a] = parent_b
            self.rank[parent_b] += self.rank[parent_a]

        return True


if __name__ == '__main__':
    edges = [[1, 2], [1, 3], [2, 3]]
    s = Solution()
    print(s.findRedundantConnection(edges))

    edges = [[1, 5], [3, 4], [3, 5], [4, 5], [2, 4]]
    s = Solution()
    print(s.findRedundantConnection(edges))
