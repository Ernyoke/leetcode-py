class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if root is None:
            return 0

        def count_good_nodes(node, current_max):
            if node is None:
                return 0

            res = 0

            if node.val >= current_max:
                res += 1

            current_max = max(current_max, node.val)

            res += count_good_nodes(node.left, current_max)
            res += count_good_nodes(node.right, current_max)

            return res

        return count_good_nodes(root, root.val)

if __name__ == '__main__':
    root = TreeNode(3, TreeNode(1),
                    TreeNode(4))

    s = Solution()
    print(s.goodNodes(root))
