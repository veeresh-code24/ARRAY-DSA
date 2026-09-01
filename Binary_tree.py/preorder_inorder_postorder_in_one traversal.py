class TreeNode:
    def __init__(self, val = 0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:

    def preo_ino_post_one_Traversal(self, root):

        stack = []

        pre = []
        ino = []
        post = []

        if root is None:
            return pre, ino, post

        stack.append((root, 1))

        while stack:
            node, state = stack.pop()

            if state == 1:
                pre.append(node.data)

                stack.append((node, 2))

                if node.left:
                    stack.append((node.left, 1))


            elif state == 2:

                ino.append(node.data)

                stack.append((node, 3))

                if node.right:
                    stack.append((node.right, 1))

            else:

                post.append(node.data)

        return [pre, ino, post]

# tree  
root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


# Create Solution object
sol = Solution()

# Call function
result = sol.preo_ino_post_one_Traversal(root)

print("Preorder :", result[0])
print("Inorder  :", result[1])
print("Postorder:", result[2])