from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] < 10:
                return digits
            digits[i] = 0
        return [1] + digits


if __name__ == '__main__':
    s = Solution()

    print(s.plusOne([9]))
    print(s.plusOne([9, 9]))
    print(s.plusOne([1, 2, 3]))
    print(s.plusOne([1, 0]))
