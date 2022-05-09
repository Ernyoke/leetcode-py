# https://leetcode.com/problems/letter-combinations-of-a-phone-number

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        ans = []

        def rec(current_index: int, current_ans: List[str]):
            if current_index >= len(digits):
                ans.append(''.join(current_ans))
            else:
                for char in phone[digits[current_index]]:
                    current_ans.append(char)
                    rec(current_index + 1, current_ans)
                    current_ans.pop()

        if len(digits) > 0:
            rec(0, [])

        return ans


if __name__ == '__main__':
    print(Solution().letterCombinations("23"))
    print(Solution().letterCombinations("2"))
    print(Solution().letterCombinations(""))
