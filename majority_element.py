# https://leetcode.com/problems/majority-element/

from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter()
        for num in nums:
            counter[num] += 1
        return counter.most_common()[0][0]

    # Boyer–Moore
    def majorityElementBM(self, nums: List[int]) -> int:
        counter = 0
        candidate = None
        for num in nums:
            if counter == 0:
                candidate = num
            counter += 1 if candidate == num else -1
        return candidate


if __name__ == '__main__':
    print(Solution().majorityElement([3, 2, 3]))
    print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))

    print(Solution().majorityElementBM([3, 2, 3]))
    print(Solution().majorityElementBM([2, 2, 1, 1, 1, 2, 2]))
