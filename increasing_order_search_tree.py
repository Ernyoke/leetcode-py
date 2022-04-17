# https://leetcode.com/problems/increasing-order-search-tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def traverse(node, lst):
            if node:
                traverse(node.left, lst)
                lst.append(TreeNode(node.val))
                traverse(node.right, lst)

        ans = []
        traverse(root, ans)

        if len(ans) > 0:
            for i in range(len(ans) - 1):
                ans[i].right = ans[i + 1]
            return ans[0]


if __name__ == '__main__':
    print(Solution().increasingBST(TreeNode(5, TreeNode(1), TreeNode(7))))
