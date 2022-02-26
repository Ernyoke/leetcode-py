# https://leetcode.com/problems/sort-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        while head is not None:
            lst.append(head.val)
            head = head.next
        lst.sort()

        prev = None
        first = None
        for val in lst:
            node = ListNode(val)
            if prev is not None:
                prev.next = node
            else:
                first = node
            prev = node

        return first


if __name__ == '__main__':
    node = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    print(Solution().sortList(node))
