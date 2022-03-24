# https://leetcode.com/problems/boats-to-save-people

from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        i, j = 0, len(people) - 1
        while i <= j:
            if limit >= people[i] + people[j]:
                i += 1
            j -= 1
            count += 1

        return count


if __name__ == '__main__':
    print(Solution().numRescueBoats([3, 2, 2, 1], 3))
    print(Solution().numRescueBoats([3, 5, 3, 4], 5))
