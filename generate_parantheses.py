# https://leetcode.com/problems/generate-parenthese

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def generate(stack, left_score, right_score):
            if len(stack) == 2 * n:
                ans.append(''.join(stack))
            else:
                for p in ['(', ')']:
                    left, right = p == '(', p == ')'
                    if left_score + left <= n and right_score + right <= left_score:
                        stack.append(p)
                        generate(stack, left_score + left, right_score + right)
                        stack.pop()

        generate([], 0, 0)
        return ans

    def generateParenthesis_2(self, n):

        def generate(p, left, right, ans):
            if left:
                generate(p + '(', left - 1, right, ans)
            if right > left:
                generate(p + ')', left, right - 1, ans)
            if not right:
                ans.append(p)
            return ans

        return generate('', n, n, [])


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))
