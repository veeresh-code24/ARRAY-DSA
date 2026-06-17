# Brute Force

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


class Solution:
    def IntersectionLL(self,head):

                    

if __name__ == '__main__':
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    fifth.next = second
    # third.next = second

sol = Solution()
startNode = sol.IntersectionLL(head)

if startNode:
    print("Loop is present in linkedList",startNode)
else:
    print("Loop is not in linkedList")
