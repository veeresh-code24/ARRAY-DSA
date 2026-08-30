class TreeNode:

    def __init__(self, val=0, left = None, right=None):
        self.data = val
        self.left = left
        self.right = right


class Solution:

    def iterative_preorder(self, root):

        preorder = []

        if  root is None:
            return preorder

        stack = [root]

        while stack:
            node = stack.pop()
            preorder.append(node.data)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return preorder

if __name__ == "__main__":
    # Creating a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    sol = Solution()

    # Getting the preorder traversal
    result = sol.iterative_preorder(root)

    # Displaying the preorder traversal result
    print("Preorder Traversal:", result)

    

    


        

    