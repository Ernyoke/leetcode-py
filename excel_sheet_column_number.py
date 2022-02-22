class Solution:
    @staticmethod
    def to_num(c):
        return ord(c) - ord('A') + 1

    def titleToNumber(self, columnTitle: str) -> int:
        s = 0
        for i, c in enumerate(columnTitle[::-1]):
            s += Solution.to_num(c) * 26 ** i

        return s


if __name__ == '__main__':
    print(Solution().titleToNumber('AB'))
    print(Solution().titleToNumber('A'))
    print(Solution().titleToNumber('ZY'))
    print(Solution().titleToNumber('FXSHRXW'))