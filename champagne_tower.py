# https://leetcode.com/problems/champagne-tower/submissions/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        n = 101

        tower = []
        for i in range(n):
            tower.append([0] * n)

        tower[0][0] = poured

        for i in range(1, n):
            any_left = False
            for j in range(i):
                if tower[i - 1][j] > 1:
                    current = tower[i - 1][j] - 1
                    tower[i][j] += current / 2
                    tower[i][j + 1] += current / 2
                    tower[i - 1][j] = 1
                    any_left = True

            if not any_left:
                break

        return tower[query_row][query_glass]


if __name__ == '__main__':
    print(Solution().champagneTower(2, 1, 1))
    print(Solution().champagneTower(100000009, 33, 17))
