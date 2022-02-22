# https://leetcode.com/problems/add-two-numbers/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        prev = ans = None

        while l1 and l2:
            value = l1.val + l2.val + carry
            if value >= 10:
                value -= 10
                carry = 1
            else:
                carry = 0

            node = ListNode(value)

            if prev is None:
                ans = node
            else:
                prev.next = node

            prev = node
            l1, l2 = l1.next, l2.next

        while l1:
            value = l1.val + carry
            if value >= 10:
                value -= 10
                carry = 1
            else:
                carry = 0

            node = ListNode(value)

            if prev is None:
                ans = node
            else:
                prev.next = node

            prev = node
            l1 = l1.next

        while l2:
            value = l2.val + carry
            if value >= 10:
                value -= 10
                carry = 1
            else:
                carry = 0

            node = ListNode(value)

            if prev is None:
                ans = node
            else:
                prev.next = node

            prev = node
            l2 = l2.next

        if carry > 0:
            prev.next = ListNode(1)

        return ans


def build(lst):
    prev = None
    first = None
    for l in lst:
        a = ListNode(l)
        if prev is None:
            first = a
        else:
            prev.next = a
        prev = a

    return first


def print_solution(l1):
    while l1:
        print(l1.val, end=' ')
        l1 = l1.next


if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]

    res = Solution().addTwoNumbers(build(l1), build(l2))
    print_solution(res)

    print()

    l3 = [9, 9, 9, 9, 9, 9, 9]
    l4 = [9, 9, 9, 9]

    res = Solution().addTwoNumbers(build(l3), build(l4))
    print_solution(res)
