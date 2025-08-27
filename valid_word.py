# https://leetcode.com/problems/valid-word


class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        has_vowel, has_consonant = False, False

        for c in word:
            if c.isalpha():
                if c.lower() in "aeiou":
                    has_vowel = True
                else:
                    has_consonant = True
            elif not c.isdigit():
                return False

        return has_consonant and has_vowel


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("asd123 asd"))
    print(s.isValid("asd123"))
