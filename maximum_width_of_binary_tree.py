# https://leetcode.com/problems/maximum-width-of-binary-tree/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 1
        queue = [(0, root)]
        while queue:
            new_queue = []
            for pw, node in queue:
                if node.left is not None:
                    new_queue.append((2 * pw, node.left))
                if node.right is not None:
                    new_queue.append((2 * pw + 1, node.right))
            ans = max(ans, new_queue[-1][0] - new_queue[0][0] + 1) if len(new_queue) >= 2 else ans
            queue = new_queue

        return ans


if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t5 = TreeNode(5)
    t6 = TreeNode(3)
    t7 = TreeNode(9)

    t1.left = t3
    t1.right = t2
    t3.left = t5
    t3.right = t6
    t2.right = t7

    print(Solution().widthOfBinaryTree(t1))
