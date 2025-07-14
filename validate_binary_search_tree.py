from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, lower, upper):
            if not node:
                return True

            if lower < node.val < upper:
                return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)

            return False

        return dfs(root, float('-inf'), float('inf'))


if __name__ == '__main__':
    s = Solution()
    node = TreeNode(10,
                    left=TreeNode(5, left=TreeNode(3), right=TreeNode(8)),
                    right=TreeNode(15))
    print(s.isValidBST(node))

    node = TreeNode(1, TreeNode(2), TreeNode(3))
    print(s.isValidBST(node))
