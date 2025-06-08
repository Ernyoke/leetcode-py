# https://leetcode.com/problems/longest-happy-string

import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res, max_heap = "", []
        for count, c in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(max_heap, (count, c))

        while max_heap:
            count, c = heapq.heappop(max_heap)
            if len(res) > 1 and res[-1] == res[-2] == c:
                if not max_heap:
                    break
                count_2, c_2 = heapq.heappop(max_heap)
                res += c_2
                count_2 += 1

                if count_2:
                    heapq.heappush(max_heap, (count_2, c_2))
            else:
                res += c
                count += 1

            if count:
                heapq.heappush(max_heap, (count, c))

        return res


if __name__ == '__main__':
    s = Solution().longestDiverseString(a=1, b=1, c=7)
    print(s)
