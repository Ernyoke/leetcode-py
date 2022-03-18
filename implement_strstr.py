# https://leetcode.com/problems/implement-strstr

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] != needle[0]:
                continue
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


if __name__ == '__main__':
    print(Solution().strStr('hello', 'll'))
    print(Solution().strStr('aaaaa', 'bba'))
    print(Solution().strStr('aaaaa', 'aaaaaaa'))
    print(Solution().strStr('', ''))
