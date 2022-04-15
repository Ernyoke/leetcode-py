# https://leetcode.com/problems/search-in-a-binary-search-tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search_rec(node):
            if node:
                if val < node.val:
                    return search_rec(node.left)
                elif val > node.val:
                    return search_rec(node.right)
                elif val == node.val:
                    return node

        return search_rec(root)


if __name__ == '__main__':
    print(Solution().searchBST(TreeNode(), 0))
