class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ans = 0
        max_num = 0
        for char in s[::-1]:
            if d[char] >= max_num:
                ans += d[char]
                max_num = d[char]
            else:
                ans -= d[char]
        return ans


if __name__ == '__main__':
    print(Solution().romanToInt('MCMXCIV'))
    print(Solution().romanToInt('LVIII'))
