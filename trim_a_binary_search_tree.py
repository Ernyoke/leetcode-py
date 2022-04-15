# https://leetcode.com/problems/trim-a-binary-search-tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        start = TreeNode(-1, right=root)
        stack = [(start, root)]
        while stack:
            parent, node = stack.pop()
            if node:
                if node.val < low:
                    if node.right:
                        if parent.val < node.right.val:
                            parent.right = node.right
                        else:
                            parent.left = node.right
                        stack.append((parent, node.right))
                    else:
                        if parent.val < node.val:
                            parent.right = None
                        else:
                            parent.left = None
                    continue

                if node.val > high:
                    if node.left:
                        if parent.val < node.left.val:
                            parent.right = node.left
                        else:
                            parent.left = node.left
                        stack.append((parent, node.left))
                    else:
                        if parent.val < node.val:
                            parent.right = None
                        else:
                            parent.left = None
                    continue

                stack.append((node, node.right))
                stack.append((node, node.left))

        return start.right


if __name__ == '__main__':
    print(Solution().trimBST(TreeNode(1, TreeNode(0), TreeNode(2)), 1, 2))
    print(Solution().trimBST(TreeNode(3, TreeNode(0, None, TreeNode(2, TreeNode(1), None)), TreeNode(4)), 1, 3))
    print(Solution().trimBST(TreeNode(1, None, TreeNode(2)), 2, 4))
    print(Solution().trimBST(TreeNode(3, TreeNode(2), TreeNode(4, TreeNode(1))), 1, 1))
