# https://leetcode.com/problems/unique-paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a = [1] * n
        b = a
        for i in range(1, m):
            b = [0] * n
            for j in range(n):
                b[j] = (0 if j - 1 < 0 else b[j - 1]) + (0 if i - 1 < 0 else a[j])
            a = b

        return b[-1]


if __name__ == '__main__':
    print(Solution().uniquePaths(3, 7))
    print(Solution().uniquePaths(3, 2))
