# leetcode.com/problems/maximum-split-of-positive-even-integers

from typing import List


class Solution:
    def maximumEvenSplit(self, final_sum: int) -> List[int]:
        if final_sum % 2 != 0:
            return []
        else:
            ans = []
            i = 2
            while True:
                final_sum -= i
                if final_sum <= i:
                    ans.append(i + final_sum)
                    break
                ans.append(i)
                i += 2
            return ans


if __name__ == '__main__':
    print(Solution().maximumEvenSplit(28))