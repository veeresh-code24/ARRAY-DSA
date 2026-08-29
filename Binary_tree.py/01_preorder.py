# ROOT --> LEFT --> RIGHT

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def preorder(self, node):

        if node is None:
            return 

        print(node.data, end=" ")

        self.preorder(node.left)

        self.preorder(node.right)


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

sol = Solution()
sol.preorder(root)


    