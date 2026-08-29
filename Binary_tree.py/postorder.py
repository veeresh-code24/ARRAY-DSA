class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:

    def postorder(self, node):

        if node is None:
            return

        self.postorder(node.left)

        self.postorder(node.right)

        print(node.data, end = ' ')

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(7)
root.right.right = Node(8)

root.left.right.left = Node(6)

root.right.right.left = Node(9)
root.right.right.right = Node(10)

sol = Solution()

sol.postorder(root)


