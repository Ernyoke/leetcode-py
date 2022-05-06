# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if not stack or stack[-1][0] != char:
                stack.append((char, 1))
            else:
                stack[-1] = (char, stack[-1][1] + 1)
                if stack[-1][1] == k:
                    stack.pop()

        return ''.join([char * n for char, n in stack])


if __name__ == '__main__':
    print(Solution().removeDuplicates('deeedbbcccbdaa', 3))
    print(Solution().removeDuplicates('pbbcggttciiippooaais', 2))
    print(Solution().removeDuplicates('abcd', 2))
