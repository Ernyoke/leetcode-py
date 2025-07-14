# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i

from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        counter = Counter(s)

        min_freq, max_freq = float("inf"), 0

        for c, freq in counter.items():
            if freq % 2 == 1:
                max_freq = max(max_freq, freq)
            else:
                min_freq = min(min_freq, freq)

        return max_freq - min_freq

if __name__ == '__main__':
    s = Solution()
    print(s.maxDifference("aaaaabbc"))
    print(s.maxDifference("abcabcab"))
    print(s.maxDifference("tzt"))