# https://leetcode.com/problems/balanced-binary-tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node) -> (bool, int):
            if node is None:
                return True, 0

            left_balanced, left_height = dfs(node.left)
            right_balanced, right_height = dfs(node.right)

            diff = abs(left_height - right_height)
            return left_balanced and right_balanced and diff <= 1, max(left_height, right_height) + 1

        res = dfs(root)
        return res[0]


if __name__ == '__main__':
    s = Solution()
    tree = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4)))
    print(s.isBalanced(tree))

    tree = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
    print(s.isBalanced(tree))
