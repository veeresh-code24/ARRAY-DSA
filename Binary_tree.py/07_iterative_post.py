class TreeNode:
    def __init__(self, val = 0, left = None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def iterative_postorder(self, root):

        stack1 = []
        stack2  = []
        postorder = []

        if root is None:
            return

        stack1.append(root)

        while stack1:

            node = stack1.pop()

            stack2.append(node)

            if node.left:
                stack1.append(node.left)

            if node.right:
                stack1.append(node.right)

        while stack2:
            node = stack2.pop()
            postorder.append(node.data)

        return postorder

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Create Solution object
sol = Solution()

# Call function
result = sol.iterative_postorder(root)

print("Postorder:", result)
