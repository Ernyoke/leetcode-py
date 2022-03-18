# https://leetcode.com/problems/remove-duplicate-letters/
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # def smallestSubsequence(self, s: str) -> str:
        counter = [0] * 26
        for char in s:
            counter[ord(char) - ord('a')] += 1

        stack = []
        visited = set()
        for char in s:
            counter[ord(char) - ord('a')] -= 1

            if char in visited:
                continue

            while stack and ord(char) < ord(stack[-1]) and counter[ord(stack[-1]) - ord('a')] >= 1:
                visited.remove(stack.pop())

            stack.append(char)
            visited.add(char)

        return ''.join(stack)


if __name__ == '__main__':
    print(Solution().removeDuplicateLetters('cbacdcbc'))
    print(Solution().removeDuplicateLetters('bbcaac'))
