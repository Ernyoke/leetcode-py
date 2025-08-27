from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            if a is None and b is None:
                return True

            if (a is None and b is not None) or (a is not None and b is None):
                return False

            if a.val != b.val:
                return False

            return dfs(a.left, b.left) and dfs(a.right, b.right)

        return dfs(p, q)


if __name__ == '__main__':
    a = TreeNode(1, TreeNode(2))
    b = TreeNode(1, None, TreeNode(2))
    s = Solution()
    print(s.isSameTree(a, b))
