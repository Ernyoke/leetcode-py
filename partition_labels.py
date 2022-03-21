# https://leetcode.com/problems/partition-labels

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for index, char in enumerate(s):
            d[char] = index if char not in d else max(d[char], index)

        max_pos, start_pos = -1, 0
        ans = []
        for index, char in enumerate(s):
            max_pos = max(max_pos, d[char])

            if max_pos == index:
                ans.append(index - start_pos + 1)
                max_pos, start_pos = -1, index + 1

        return ans


if __name__ == '__main__':
    print(Solution().partitionLabels('ababcbacadefegdehijhklij'))
    print(Solution().partitionLabels('eccbbbbdec'))
    print(Solution().partitionLabels('abcdaeeeffeg'))
