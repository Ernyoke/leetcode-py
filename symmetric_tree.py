# https://leetcode.com/problems/symmetric-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def traverse(a: TreeNode, b: TreeNode):
            if a is None and b is None:
                return True

            if (a is None and b is not None) or (a is not None and b is None) or a.val != b.val:
                return False

            return traverse(a.left, b.right) and traverse(a.right, b.left)

        return traverse(root.left, root.right)


if __name__ == '__main__':
    print(Solution().isSymmetric(TreeNode(0, TreeNode(1), TreeNode(1))))
