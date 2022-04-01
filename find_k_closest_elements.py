# https://leetcode.com/problems/find-k-closest-elements

import bisect
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        position = min(bisect.bisect_left(arr, x), len(arr) - 1)

        ans = []
        left, right = position, position - 1

        for i in range(k):
            if left - 1 >= 0 and right + 1 < len(arr):
                a, b = arr[left - 1], arr[right + 1]
                if abs(a - x) == abs(b - x):
                    if a < b:
                        ans.append(a)
                        left -= 1
                    else:
                        ans.append(b)
                        right += 1
                elif abs(a - x) < (b - x):
                    ans.append(a)
                    left -= 1
                else:
                    ans.append(b)
                    right += 1
            elif left - 1 >= 0:
                ans.append(arr[left - 1])
                left -= 1
            else:
                ans.append(arr[right + 1])
                right += 1

        ans.sort()
        return ans


if __name__ == '__main__':
    print(Solution().findClosestElements([1, 2, 3, 4, 5], 4, 3))
    print(Solution().findClosestElements([1, 2, 3, 4, 5], 4, -1))
    print(Solution().findClosestElements([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5))
