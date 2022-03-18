# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        i = j = 0
        max_len = 0
        while i < len(s):
            c = s[i]
            if c in d:
                max_len = max(i - j, max_len)
                end = d[c]
                while j <= end:
                    del d[s[j]]
                    j += 1

            d[c] = i
            i += 1

        max_len = max(i - j, max_len)

        return max_len


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('abcabcbb'))
    print(Solution().lengthOfLongestSubstring('bbbbb'))
    print(Solution().lengthOfLongestSubstring('aaabcdeeeeea'))
    print(Solution().lengthOfLongestSubstring('a'))
