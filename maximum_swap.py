# https://leetcode.com/problems/maximum-swap/
from typing import List


def to_int(nums: List[int]) -> int:
    res = 0
    for num in nums:
        res = res * 10 + num
    return res


def to_digits(num: int) -> List[int]:
    if num == 0:
        return [0]

    res = []

    while num > 0:
        mod = num % 10
        res.append(mod)
        num = num // 10

    res.reverse()
    return res


class Solution:

    def maximumSwap(self, num: int) -> int:
        digits = to_digits(num)
        max_val, max_pos = digits[len(digits) - 1], len(digits) - 1
        swap_i, swap_j = len(digits) - 1, len(digits) - 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < digits[max_pos]:
                swap_i = i
                swap_j = max_pos
                continue
            if digits[i] > digits[max_pos]:
                max_pos = i

        digits[swap_j], digits[swap_i] = digits[swap_i], digits[swap_j]
        return to_int(digits)


if __name__ == '__main__':
    print(Solution().maximumSwap(2736))
    print(Solution().maximumSwap(9973))
