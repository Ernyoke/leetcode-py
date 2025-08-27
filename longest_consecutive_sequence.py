# https://leetcode.com/problems/longest-consecutive-sequence

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        longest = 0

        while s:
            num = s.pop()
            current_longest = 1

            left = num - 1

            while left in s:
                s.remove(left)
                left -= 1
                current_longest += 1

            right = num + 1
            while right in s:
                s.remove(right)
                right += 1
                current_longest += 1

            longest = max(longest, current_longest)

        return longest


if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    s = Solution()
    print(s.longestConsecutive(nums))
