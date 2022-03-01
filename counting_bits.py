# https://leetcode.com/problems/counting-bits

from typing import List


class Solution:
    def countBits_slow(self, n: int) -> List[int]:
        return [sum([1 if bit == '1' else 0 for bit in f'{num:b}']) for num in range(n + 1)]

    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans


if __name__ == '__main__':
    print(Solution().countBits(5))
