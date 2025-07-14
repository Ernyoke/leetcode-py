# https://leetcode.com/problems/find-the-original-typed-string-i

from collections import Counter


class Solution:
    def possibleStringCount(self, word: str) -> int:
        counter = Counter()
        prev = None
        prev_i = None
        for i, c in enumerate(word):
            if prev == c:
                counter[(prev, prev_i)] += 1
            else:
                prev = c
                prev_i = i
                counter[(prev, prev_i)] += 1

        res = 1
        for ch, count in counter.items():
            if count > 1:
                res += (count - 1)

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.possibleStringCount("abbcccc"))
    print(s.possibleStringCount("aaaa"))
    print(s.possibleStringCount("abcd"))
