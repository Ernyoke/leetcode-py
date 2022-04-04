# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {n}

        while n != 1:
            sum_n = 0

            while n > 0:
                digit = n % 10
                n //= 10
                sum_n += (digit * digit)

            if sum_n in seen:
                return False

            seen.add(sum_n)
            n = sum_n

        return True


if __name__ == '__main__':
    print(Solution().isHappy(19))
    print(Solution().isHappy(2))
