class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        aux = x
        y = 0
        while aux:
            y = y * 10 + aux % 10
            aux //= 10
        return x == y


if __name__ == '__main__':
    print(Solution().isPalindrome(10))
    print(Solution().isPalindrome(101))
