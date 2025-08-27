# https://leetcode.com/problems/most-beautiful-item-for-each-query

from typing import List


def binary_search(items, target_price):
    left, right = 0, len(items) - 1
    max_beauty = 0
    while left <= right:
        mid = (left + right) // 2
        if items[mid][0] > target_price:
            right = mid - 1
        else:
            max_beauty = max(max_beauty, items[mid][1])
            left = mid + 1
    return max_beauty


class Solution:
    def maximumBeauty(elf, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: x[0])

        max_beauty = items[0][1]
        for i in range(len(items)):
            max_beauty = max(max_beauty, items[i][1])
            items[i][1] = max_beauty

        return [binary_search(items, q) for q in queries]


if __name__ == '__main__':
    s = Solution()
    items = [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]]
    queries = [1, 2, 3, 4, 5, 6]
    print(s.maximumBeauty(items, queries))

    items = [[1, 2], [1, 2], [1, 3], [1, 4]]
    queries = [1]
    print(s.maximumBeauty(items, queries))

    items = [[10, 1000]]
    queries = [5]
    print(s.maximumBeauty(items, queries))

    items = [[193, 732], [781, 962], [864, 954], [749, 627], [136, 746], [478, 548], [640, 908], [210, 799], [567, 715],
             [914, 388], [487, 853], [533, 554], [247, 919], [958, 150], [193, 523], [176, 656], [395, 469], [763, 821],
             [542, 946], [701, 676]]
    queries = [885, 1445, 1580, 1309, 205, 1788, 1214, 1404, 572, 1170, 989, 265, 153, 151, 1479, 1180, 875, 276, 1584]
    print(s.maximumBeauty(items, queries))
