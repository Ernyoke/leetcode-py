# https://leetcode.com/problems/convert-bst-to-greater-tree
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder_traverse(node, lst):
            if node:
                inorder_traverse(node.left, lst)
                lst.append(node)
                inorder_traverse(node.right, lst)

        nodes = []
        inorder_traverse(root, nodes)

        prefix_sum = 0
        for node in nodes[::-1]:
            node.val += prefix_sum
            prefix_sum = node.val

        return root


if __name__ == '__main__':
    print(Solution().convertBST(TreeNode()))
