# https://leetcode.com/problems/maximum-product-of-word-lengths

from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d = dict()
        for word in words:
            value = 0
            for char in word:
                value |= (1 << (ord(char) - ord('a') + 1))
            d[value] = len(word) if value not in d else max(len(word), d[value])

        max_value = 0
        for value, length in d.items():
            for value_2, length_2 in d.items():
                if (value & value_2) <= 0:
                    max_value = max(length * length_2, max_value)
        return max_value


if __name__ == '__main__':
    print(Solution().maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
    print(Solution().maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))
    print(Solution().maxProduct(["a", "aa", "aaa", "aaaa"]))
