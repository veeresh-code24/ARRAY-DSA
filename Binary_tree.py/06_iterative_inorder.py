class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


class Solution:

    def iterative_inorder(self, root):
        inorder = []
        stack = []

        node = root

        while True:

            if node is not None:
                stack.append(node)
                node = node.left

            else:

                if not stack:
                    break

                node = stack.pop()

                inorder.append(node.data)

                node = node.right

        return inorder

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

sol = Solution()

result = sol.iterative_inorder(root)

print(result)











