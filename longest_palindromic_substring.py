# https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        d = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            d[i][i] = True

        max_palindrome = (0, 0)

        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[j] == s[i]:
                    d[i][j] = d[i + 1][j - 1] if j - i > 1 else True

                    if d[i][j] and j - i > max_palindrome[1] - max_palindrome[0]:
                        max_palindrome = (i, j)

        return s[max_palindrome[0]:max_palindrome[1] + 1]


if __name__ == '__main__':
    print(Solution().longestPalindrome('babad'))
    print(Solution().longestPalindrome('cbbd'))
    print(Solution().longestPalindrome('aaaa'))