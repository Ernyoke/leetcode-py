import copy
from typing import List


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def recourse(current: List[str], s: str):
            if not s:
                res.append(copy.copy(current))
                return

            for i in range(1, len(s) + 1):
                part = s[:i]
                if is_palindrome(part):
                    current.append(part)
                    recourse(current, s[i:])
                    current.pop()

        recourse([], s)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.partition("aab"))
