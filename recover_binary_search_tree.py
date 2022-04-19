# https://leetcode.com/problems/recover-binary-search-tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:
    def __init__(self):
        self.prev_node = None
        self.first = self.second = None

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def traverse(node):
            if node:
                traverse(node.left)
                if self.first is None and self.prev_node and self.prev_node.val > node.val:
                    self.first = self.prev_node
                if self.first is not None and self.prev_node and self.prev_node.val > node.val:
                    self.second = node
                self.prev_node = node
                traverse(node.right)

        traverse(root)
        self.first.val, self.second.val = self.second.val, self.first.val


if __name__ == '__main__':
    tree = TreeNode(3, TreeNode(1), TreeNode(4, TreeNode(2)))
    Solution().recoverTree(tree)
    print(tree)

    tree = TreeNode(1, left=TreeNode(3, right=TreeNode(2)))
    Solution().recoverTree(tree)
    print(tree)
