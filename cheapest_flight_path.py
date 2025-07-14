# https://neetcode.io/problems/cheapest-flight-path

from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            is_change = False
            tmp_prices = prices.copy()
            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue

                if tmp_prices[d] > prices[s] + p:
                    tmp_prices[d] = prices[s] + p
                    is_change = True
            prices = tmp_prices

            if not is_change:
                break

        return -1 if prices[dst] == float("inf") else prices[dst]


if __name__ == '__main__':
    s = Solution()
    n = 3
    flights = [[1, 0, 100], [1, 2, 200], [0, 2, 100]]
    src = 1
    dst = 2
    k = 1

    print(s.findCheapestPrice(n, flights, src, dst, k))
