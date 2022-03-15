# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        to_remove = set()
        for index, char in enumerate(s):
            if char == ')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(index)
            elif char == '(':
                stack.append(index)

        to_remove.update(stack)

        ans = []
        for index, char in enumerate(s):
            if index not in to_remove:
                ans.append(char)

        return ''.join(ans)


if __name__ == '__main__':
    print(Solution().minRemoveToMakeValid('lee(t(c)o)de)'))
    print(Solution().minRemoveToMakeValid('a)b(c)d'))
    print(Solution().minRemoveToMakeValid('))(('))
