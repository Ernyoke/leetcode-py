# https://leetcode.com/problems/minimum-depth-of-binary-tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            if node.right is None and node.left is None:
                return 1

            l = float("inf")
            if node.left:
                l = dfs(node.left)

            r = float("inf")
            if node.right:
                r = dfs(node.right)

            return 1 + min(l, r)

        if root:
            return dfs(root)
        return 0


if __name__ == '__main__':
    node = TreeNode(2, None, TreeNode(3, None, TreeNode(4)))
    s = Solution()
    print(s.minDepth(node))
