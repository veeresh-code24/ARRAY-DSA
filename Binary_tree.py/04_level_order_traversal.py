'''from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


class Solution:
    def level_order_traversal(self,root):
        ans =[]
        if not root:
            return ans

        q = deque([root])

        while q:
            level = []

            for _ in range(len(q)):

                node = q.popleft()
                level.append(node.data)

                if node.left:
                    q.ap2pend(node.left)

                if node.right:
                    q.append(node.right)

            ans.append(level)

        return ans

def PrintList(lst):

    for num in lst:
        print(num, end=" ")

    print()

if __name__ == "__main__":

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    sol = Solution()

    result = sol.level_order_traversal(root)

    print("Level order of Traversal")

    for level in result:
        PrintList(level)'''


    



    





    

        