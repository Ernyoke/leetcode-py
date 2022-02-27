# https://leetcode.com/problems/remove-nth-node-from-end-of-list
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}'


def reverse(head):
    tail = None
    while head is not None:
        if tail is None:
            tail = ListNode(head.val)
        else:
            prev = tail
            tail = ListNode(head.val)
            tail.next = prev
        head = head.next
    return tail


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tail = reverse(head)
        first = tail

        if n == 1:
            first = tail.next
        else:
            for i in range(1, n - 1):
                if tail is None:
                    break
                tail = tail.next

            if tail.next is not None:
                tail.next = tail.next.next

        head = reverse(first)
        return head


if __name__ == '__main__':
    h = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(Solution().removeNthFromEnd(h, 2))

    h = ListNode(1, ListNode(2))
    print(Solution().removeNthFromEnd(h, 1))