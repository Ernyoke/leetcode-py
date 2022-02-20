class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for c in s:
            d.setdefault(c, 0)
            d[c] += 1
        return ''.join(sorted(list(s), key=lambda v: (-d[v], v)))


if __name__ == '__main__':
    print(Solution().frequencySort('tree'))