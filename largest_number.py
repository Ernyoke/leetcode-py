from typing import List
from functools import cmp_to_key


def compare(a: str, b: str) -> int:
    a1 = a + b
    b1 = b + b
    if a1 < b1:
        return 1
    elif a1 > b1:
        return -1
    return 0


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        sorted_nums = sorted([str(num) for num in nums], key=(cmp_to_key(compare)))

        if all([True if num == 0 else False for num in nums]):
            return "0"

        return "".join(sorted_nums)


if __name__ == '__main__':
    s = Solution().largestNumber([1111, 12, 3, 30, 34, 5, 9])
    print(s)

    s = Solution().largestNumber([432,43243])
    print(s)

    s = Solution().largestNumber([111311,1113])
    print(s)

    s = Solution().largestNumber([0,0])
    print(s)

