# https://leetcode.com/problems/binary-tree-inorder-traversal

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(node, lst):
            if node:
                traverse(node.left, lst)
                lst.append(node.val)
                traverse(node.right, lst)

        ans = []
        traverse(root, ans)
        return ans


if __name__ == '__main__':
    print(Solution().inorderTraversal(TreeNode()))
