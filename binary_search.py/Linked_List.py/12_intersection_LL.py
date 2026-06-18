class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


class Solution:
    def IntersectionLL(self,headA,headB):

        tempA = headA

        while tempA:
            tempB = headB

            while tempB:
                if tempA == tempB:
                    return tempA

                tempB = tempB.next

            tempA = tempA.nexts

        return None


if __name__ == '__main__':

        # Common part
        common1 = Node(8)  
        common2 = Node(10)

        common1.next = common2

        # First Linked List: 1 -> 2 -> 8 -> 10

        headA = Node(1)
        secondA = Node(2)

        headA.next = secondA
        secondA.next = common1

        # Second Linked List: 3 -> 8 -> 10
        headB = Node(3)

        headB.next = common1

        sol = Solution()
        intersectionNode = sol.IntersectionLL(headA,headB)

        if intersectionNode:
            print("Intersection Node:", intersectionNode.data)
        else:
            print("No Intersection")
    



