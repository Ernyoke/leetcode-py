# https://leetcode.com/problems/path-sum-ii

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node: Optional[TreeNode], current_sum, path: List[int]):
            if node is None:
                return

            current_sum += node.val
            path = path + [node.val]

            if current_sum == targetSum and node.left is None and node.right is None:
                res.append(path)
                return

            dfs(node.left, current_sum, path)
            dfs(node.right, current_sum, path)

        dfs(root, 0, [])

        return res


if __name__ == '__main__':
    s = Solution()
    tree = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
                    TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))

    res = s.pathSum(tree, 22)
    print(res)
