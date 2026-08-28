class Node:
    def __init__(self,key):
        self.data  = key
        self.left = None
        self.right = None


class Solution:
    def create_binary_tree(self):

        root = Node(1)

        root.left = Node(2)

        root.right = Node(3)

        root.right.left = Node(5)

        return root
    
solution = Solution()
root = solution.create_binary_tree()
print(root.data)
print(root.left.data)
print(root.right.data)
print(root.right.left.data)

