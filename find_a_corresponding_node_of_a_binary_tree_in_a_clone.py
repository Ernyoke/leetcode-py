# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def dfs(node, cloned_node):
            if not node:
                return
            if node == target:
                return cloned_node
            ans = dfs(node.left, cloned_node.left)
            if ans:
                return ans
            else:
                return dfs(node.right, cloned_node.right)

        return dfs(original, cloned)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    cloned = TreeNode(1)
    cloned.left = TreeNode(2)
    cloned.right = TreeNode(3)
    print(Solution().getTargetCopy(root, cloned, root.right))
