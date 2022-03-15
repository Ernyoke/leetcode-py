# https://leetcode.com/problems/group-anagrams

from itertools import groupby
from operator import itemgetter
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return [list(map(itemgetter(1), value)) for key, value in
                groupby(sorted(map(lambda s: ("".join(sorted(s)), s), strs)), itemgetter(0))]


if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
