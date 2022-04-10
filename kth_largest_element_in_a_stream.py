# https://leetcode.com/problems/kth-largest-element-in-a-stream

import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums[:]
        heapq.heapify(self.nums)

        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]


if __name__ == '__main__':
    kth_1 = KthLargest(3, [4, 5, 8, 2])
    print(kth_1.add(3))
    print(kth_1.add(5))
    print(kth_1.add(10))
    print(kth_1.add(9))
    print(kth_1.add(4))

    kth_2 = KthLargest(1, [])
    print(kth_2.add(-3))
    print(kth_2.add(-2))
    print(kth_2.add(-4))
    print(kth_2.add(0))
    print(kth_2.add(4))

    kth_3 = KthLargest(2, [0])
    print(kth_3.add(-1))
    print(kth_3.add(1))
    print(kth_3.add(-2))
    print(kth_3.add(-4))
    print(kth_3.add(3))
