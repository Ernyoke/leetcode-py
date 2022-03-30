# https://leetcode.com/problems/search-a-2d-matrix/submissions/

import itertools
from bisect import bisect_left
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lst = list(itertools.chain.from_iterable(matrix))
        pos = bisect_left(lst, target)
        return lst[pos] == target if 0 <= pos < len(lst) else False


if __name__ == '__main__':
    print(Solution().searchMatrix([[1]], 2))
