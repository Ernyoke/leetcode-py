# https://leetcode.com/problems/swapping-nodes-in-a-linked-list

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        n = 0
        current = left = head
        while current is not None:
            if n == k - 1:
                left = current
            current = current.next
            n += 1

        i = 0
        right = current = head
        while current is not None:
            if i == n - k:
                right = current
                break
            current = current.next
            i += 1

        left.val, right.val = right.val, left.val

        return head


if __name__ == '__main__':
    print(Solution().swapNodes(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2))
    print(Solution().swapNodes(ListNode(1), 1))
    print(Solution().swapNodes(ListNode(1, ListNode(2)), 1))
    print(Solution().swapNodes(ListNode(100, ListNode(90)), 2))
