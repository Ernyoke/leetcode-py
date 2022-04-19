# https://leetcode.com/problems/kth-smallest-element-in-a-bst

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lst = []

        def traverse(node):
            if len(lst) >= k:
                return lst[k - 1]
            else:
                if node:
                    res = traverse(node.left)
                    if not res:
                        lst.append(node.val)
                        res = traverse(node.right)
                    return res

        return traverse(root)


if __name__ == '__main__':
    print(Solution().kthSmallest(TreeNode(3, TreeNode(1, right=TreeNode(2)), TreeNode(4)), 1))
