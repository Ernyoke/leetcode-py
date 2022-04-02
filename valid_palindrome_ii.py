# https://leetcode.com/problems/valid-palindrome-ii

class Solution:
    def isPalindrom(self, s: str):
        return s == s[::-1]

    def validPalindrome(self, s: str) -> bool:
        a, b = 0, len(s) - 1
        while a < b:
            if s[a] != s[b]:
                return self.isPalindrom(s[a:b]) or self.isPalindrom(s[a + 1:b + 1])
            a += 1
            b -= 1

        return True


if __name__ == '__main__':
    print(Solution().validPalindrome('abca'))
    print(Solution().validPalindrome('aba'))
