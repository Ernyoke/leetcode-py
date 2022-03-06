# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options

from math import factorial

X = 10 ** 9 + 7


class Solution:
    def countOrders(self, n: int) -> int:
        return (factorial(2 * n) // 2 ** n) % X


if __name__ == '__main__':
    print(Solution().countOrders(3))
