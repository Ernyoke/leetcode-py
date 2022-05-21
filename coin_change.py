# https://leetcode.com/problems/coin-change

import sys
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amounts = [sys.maxsize] * (amount + 1)
        amounts[0] = 0
        coins.sort()
        for i in range(1, len(amounts)):
            for coin in coins:
                if i - coin < 0:
                    break
                amounts[i] = min(amounts[i - coin] + 1, amounts[i])

        return amounts[amount] if amounts[amount] < sys.maxsize else -1


if __name__ == '__main__':
    print(Solution().coinChange([1, 2, 5], 11))
    print(Solution().coinChange([2], 3))
    print(Solution().coinChange([2, 1, 3], 3))
    print(Solution().coinChange([474, 83, 404, 3], 264))
