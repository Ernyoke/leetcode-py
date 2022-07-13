# https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def dfs(node, level):
            if node:
                if len(result) <= level:
                    result.append([])
                result[level].append(node.val)
                dfs(node.left, level + 1)
                dfs(node.right, level + 1)

        dfs(root, 0)

        return result


if __name__ == '__main__':
    print(Solution().levelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(17)))))
    print(Solution().levelOrder(TreeNode(1)))
