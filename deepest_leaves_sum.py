# https://leetcode.com/problems/deepest-leaves-sum

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        def preorder(node: TreeNode, level: int, current):
            current_sum, max_level = current
            nxt = current
            if node:
                if level > max_level:
                    nxt = (node.val, level)
                elif level == max_level:
                    nxt = (current_sum + node.val, level)

                nxt = preorder(node.left, level + 1, nxt)
                return preorder(node.right, level + 1, nxt)
            else:
                return nxt

        return preorder(root, 0, (0, 0))[0]


if __name__ == '__main__':
    print(Solution().deepestLeavesSum(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(6)))))
