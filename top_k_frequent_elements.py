# https://leetcode.com/problems/top-k-frequent-elements

import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [pair[0] for pair in collections.Counter(nums).most_common(k)]


if __name__ == '__main__':
    print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
    print(Solution().topKFrequent([1], 1))
