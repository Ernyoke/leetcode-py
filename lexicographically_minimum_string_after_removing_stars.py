# https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars

class Solution:
    def clearStars(self, s: str) -> str:
        stacks = [[] for _ in range(26)]

        for i, c in enumerate(s):
            if c == '*':
                for stack in stacks:
                    if stack:
                        stack.pop()
                        break
                continue
            stacks[ord(c) - ord('a')].append(i)

        res = ['*' for _ in range(len(s))]
        for c_ord, stack in enumerate(stacks):
            for i in stack:
                res[i] = chr(c_ord + ord('a'))

        return "".join(c if c != '*' else '' for c in res)


if __name__ == '__main__':
    s = Solution().clearStars("aaba*")
    print(s)
