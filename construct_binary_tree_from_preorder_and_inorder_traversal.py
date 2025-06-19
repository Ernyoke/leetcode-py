from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def preorder(self) -> List[int]:
        res = []

        def inner(root):
            if root is not None:
                res.append(root.val)
                inner(root.left)
                inner(root.right)

        inner(self)

        return res

    def __repr__(self):
        return f"{self.preorder()}"


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)

        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root


if __name__ == "__main__":
    s = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    tree = s.buildTree(preorder, inorder)
    print(tree)