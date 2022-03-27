# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix

from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        power = [(sum(p), index) for index, p in enumerate(mat)]
        power.sort()
        return [index for p, index in power[:k]]


if __name__ == '__main__':
    print(Solution().kWeakestRows([[1, 1, 0, 0, 0],
                                   [1, 1, 1, 1, 0],
                                   [1, 0, 0, 0, 0],
                                   [1, 1, 0, 0, 0],
                                   [1, 1, 1, 1, 1]], 3))

    print(Solution().kWeakestRows([[1, 0, 0, 0],
                                   [1, 1, 1, 1],
                                   [1, 0, 0, 0],
                                   [1, 0, 0, 0]], 3))
