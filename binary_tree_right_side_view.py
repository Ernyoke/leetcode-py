# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'({self.val})'


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root is None:
            return ans

        d = deque([root])
        while d:
            size = len(d)
            for i in range(size):
                current = d.popleft()
                if i == size - 1:
                    ans.append(current.val)
                if current.left is not None:
                    d.append(current.left)
                if current.right is not None:
                    d.append(current.right)

        return ans


if __name__ == "__main__":
    sol = Solution()
    ans = sol.rightSideView(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4, None, None))))
    print(ans)
