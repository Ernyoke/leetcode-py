# https://leetcode.com/problems/copy-list-with-random-pointer

from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_head = copy_tail = None
        if head is None:
            return copy_head

        d = {}
        current = head
        while current is not None:
            prev, copy_tail = copy_tail, Node(current.val)

            if prev is not None:
                prev.next = copy_tail
            else:
                copy_head = copy_tail

            d[current] = copy_tail
            current = current.next

        current, copy_tail = head, copy_head

        while current is not None:
            if current.random is not None:
                copy_tail.random = d[current.random]
            current = current.next
            copy_tail = copy_tail.next

        return copy_head


if __name__ == '__main__':
    node1 = Node(7)
    node2 = Node(13)
    node3 = Node(11)
    node4 = Node(10)
    node5 = Node(1)

    node1.next = node2
    node1.random = None

    node2.next = node3
    node2.random = node1

    node3.next = node4
    node3.random = None

    node4.next = node5
    node4.random = node3

    node5.random = node1

    print(Solution().copyRandomList(node1))
