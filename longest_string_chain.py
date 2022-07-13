# https://leetcode.com/problems/longest-string-chain

from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        d = {}

        for word in sorted(words, key=len):
            d[word] = max(d.get(word[:i] + word[i + 1:], 0) + 1 for i in range(len(word)))

        return max(d.values())


if __name__ == '__main__':
    print(Solution().longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]))
