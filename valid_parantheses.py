# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        p = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        stack = []
        for char in s:
            if char in p:
                stack.append(p[char])
            else:
                if not stack or char != stack.pop():
                    return False
        return not stack


if __name__ == '__main__':
    print(Solution().isValid('()[]{}'))
    print(Solution().isValid('([)]'))
    print(Solution().isValid(']'))
