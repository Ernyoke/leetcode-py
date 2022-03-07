# https://leetcode.com/problems/merge-two-sorted-lists

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = None
        first = None
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                value = list1.val
                list1 = list1.next
            else:
                value = list2.val
                list2 = list2.next
            if ans is None:
                ans = ListNode(value)
                first = ans
            else:
                ans.next = ListNode(value)
                ans = ans.next

        while list1 is not None:
            if ans is None:
                ans = ListNode(list1.val)
                first = ans
            else:
                ans.next = ListNode(list1.val)
                ans = ans.next
            list1 = list1.next

        while list2 is not None:
            if ans is None:
                ans = ListNode(list2.val)
                first = ans
            else:
                ans.next = ListNode(list2.val)
                ans = ans.next
            list2 = list2.next

        return first


if __name__ == '__main__':
    print(Solution().mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4)))))
