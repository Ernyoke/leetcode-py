class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        values = [1 for _ in range(n)]
        k -= n

        for i in range(n - 1, -1, -1):
            if k - 25 >= 0:
                values[i] += 25
                k -= 25
            else:
                values[i] += k
                break

        return ''.join(map(lambda v: chr(96 + v), values))


if __name__ == '__main__':
    print(Solution().getSmallestString(3, 27))
    print(Solution().getSmallestString(5, 73))
