# https://leetcode.com/problems/divide-two-integers/

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sig = (dividend < 0) == (divisor < 0)
        a, b, res = abs(dividend), abs(divisor), 0
        while a >= b:
            x = 0
            while a >= b << (x + 1):
                x += 1
            res += 1 << x
            a -= b << x
        return min(res if sig else -res, 2 ** 31 - 1)


if __name__ == '__main__':
    print(Solution().divide(10, 3))
    print(Solution().divide(7, -3))
    print(Solution().divide(2, 2))
    print(Solution().divide(-2147483648, -1))
