# https://leetcode.com/problems/trapping-rain-water

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        current_max = height[0]
        water = [0] * len(height)
        for i, h in enumerate(height):
            current_max = max(current_max, h)
            water[i] = current_max

        current_max = height[-1]
        for i in range(len(height) - 1, -1, -1):
            current_max = max(current_max, height[i])
            water[i] = min(current_max, water[i]) - height[i]

        return sum(water)


if __name__ == '__main__':
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(Solution().trap([4, 2, 0, 3, 2, 5]))
