# https://leetcode.com/problems/baseball-game

from typing import List
import re


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record = []
        r = re.compile(r'^[-+]?[0-9]+$')
        for op in ops:
            if r.match(op):
                record.append(int(op))
            elif op == "+":
                record.append(record[-1] + record[-2])
            elif op == "C":
                record.pop()
            elif op == "D":
                record.append(record[-1] * 2)

        return sum(record)


if __name__ == '__main__':
    print(Solution().calPoints(["5", "2", "C", "D", "+"]))
    print(Solution().calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
