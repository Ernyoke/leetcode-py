# https://leetcode.com/problems/permutation-in-string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0 for _ in range(26)]
        s2_count = [0 for _ in range(26)]

        for c in s1:
            s1_count[ord(c) - ord('a')] += 1

        for i in range(len(s1)):
            s2_count[ord(s2[i]) - ord('a')] += 1

        count_match = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                count_match += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if count_match == 26:
                return True

            index = ord(s2[r]) - ord('a')
            s2_count[index] += 1

            if s1_count[index] == s2_count[index]:
                count_match += 1
            elif s1_count[index] + 1 == s2_count[index]:
                count_match -= 1

            index = ord(s2[l]) - ord('a')
            s2_count[index] -= 1

            if s1_count[index] == s2_count[index]:
                count_match += 1
            elif s1_count[index] - 1 == s2_count[index]:
                count_match -= 1

            l += 1

        return count_match == 26


if __name__ == '__main__':
    s = Solution()
    print(s.checkInclusion('ab', 'eidboaoo'))

    s = Solution()
    print(s.checkInclusion('adc', 'dcda'))

    s = Solution()
    print(s.checkInclusion('hello', 'ooolleoooleh'))

    s = Solution()
    print(s.checkInclusion('a', 'ab'))
