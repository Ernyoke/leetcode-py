# https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/

# Not tested on leetcode, since it requires subscription!

from collections import defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None, column=0):
        self.val = val
        self.left = left
        self.right = right
        self.column = column

    def __repr__(self):
        return f'({self.val})'


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = [root]
        col_by_node = defaultdict(list)

        while stack:
            node = stack.pop(0)
            col_by_node[node.column].append(node)
            if node.left:
                stack.append(node.left)
                node.left.column = node.column - 1
            if node.right:
                stack.append(node.right)
                node.right.column = node.column + 1

        sorted_by_cols = dict(sorted(col_by_node.items()))

        return [[nd.val for nd in lst] for lst in sorted_by_cols.values()]


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1, left=TreeNode(2), right=TreeNode(3, left=TreeNode(4), right=TreeNode(5, left=TreeNode(6))))

    ans = sol.verticalOrder(root)
    print(ans)
