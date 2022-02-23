# https://leetcode.com/problems/clone-graph/

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return f'{str(self.val)}'


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        first = clone = None
        stack = [(clone, node)]
        touched = set()
        d = {}
        while stack:
            parent_clone, current = stack.pop()
            if current not in touched:
                clone = Node(current.val, [])
                d[current.val] = clone
                touched.add(current)
                if first is None:
                    first = clone
            else:
                clone = d[current.val]
            if parent_clone is not None:
                parent_clone.neighbors.append(clone)
                clone.neighbors.append(parent_clone)
            for n in current.neighbors:
                if n not in touched:
                    stack.append((clone, n))
        return first



if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n3, n1]

    print(Solution().cloneGraph(n1))
    print(Solution().cloneGraph(n1))
