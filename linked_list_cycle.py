# https://leetcode.com/problems/linked-list-cycle/

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        head1 = head
        if head.next is None or head.next.next is None:
            return False
        else:
            head2 = head.next.next
        while head1 is not None and head2 is not None:
            if head1 == head2:
                return True
            else:
                if head1.next is None:
                    return False
                else:
                    head1 = head1.next

                if head2.next is None or head2.next.next is None:
                    return False
                else:
                    head2 = head2.next.next


if __name__ == '__main__':
    lst1 = ListNode(1)

    print(Solution().hasCycle(lst1))
    print(Solution().hasCycle(None))
