# https://leetcode.com/problems/count-sorted-vowel-strings

class Solution:
    def countVowelStrings(self, n: int) -> int:
        a = e = i = o = u = 1
        while n > 1:
            a = a + e + i + o + u
            e = e + i + o + u
            i = i + o + u
            o = o + u
            u = u

            n -= 1

        return a + e + i + o + u


if __name__ == '__main__':
    print(Solution().countVowelStrings(33))
