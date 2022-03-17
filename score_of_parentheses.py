# https://leetcode.com/problems/score-of-parentheses

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        current = 0

        for char in s:
            if char == '(':
                stack.append(current)
                current = 0
            else:
                current = max(1, 2 * current) + stack.pop()

        return current


if __name__ == '__main__':
    print(Solution().scoreOfParentheses('((()))()()'))
