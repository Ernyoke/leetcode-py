# https://leetcode.com/problems/rotate-list

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head

        size = 1
        last = head
        while last.next is not None:
            last = last.next
            size += 1

        k %= size

        last.next = head

        prev = None
        for i in range(size - k):
            prev = head
            head = head.next

        prev.next = None

        return head


if __name__ == '__main__':
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(Solution().rotateRight(l, 2))
