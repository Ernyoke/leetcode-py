# https://leetcode.com/problems/bulb-switcher

import math


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))


if __name__ == '__main__':
    print(Solution().bulbSwitch(1000))