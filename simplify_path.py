# https://leetcode.com/problems/simplify-path

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for part in [part for part in path.split('/') if part not in ['', '.']]:
            if part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return f"/{'/'.join(stack)}"


if __name__ == '__main__':
    print(Solution().simplifyPath('/home/p1/p2/p3/../p4'))
    print(Solution().simplifyPath('/home//foo/'))
    print(Solution().simplifyPath('/../'))
    print(Solution().simplifyPath('/a/./b/../../c/'))
