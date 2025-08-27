# https://leetcode.com/problems/flatten-binary-tree-to-linked-list

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        current = TreeNode()

        def traverse_preorder(node: TreeNode):
            nonlocal current

            if node is None:
                return

            left = node.left
            right = node.right

            current.left = None
            current.right = node
            current = current.right

            traverse_preorder(left)
            traverse_preorder(right)

        traverse_preorder(root)


if __name__ == '__main__':
    s = Solution()
    tree = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
    s.flatten(tree)

    print(tree)
