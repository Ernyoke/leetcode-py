# https://leetcode.com/problems/two-city-scheduling/

from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda a: (a[0] - a[1]))
        n = len(costs) // 2
        return sum([a[0] for a in costs[:n]]) + sum([a[1] for a in costs[n:]])


if __name__ == '__main__':
    print(Solution().twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]))
    print(Solution().twoCitySchedCost(
        [[515, 563], [451, 713], [537, 709], [343, 819], [855, 779], [457, 60], [650, 359], [631, 42]]))
