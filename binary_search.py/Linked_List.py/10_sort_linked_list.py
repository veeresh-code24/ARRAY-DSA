# Brute Force

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


class Solution:
    def sort_LL(self,head):
        if head == None or head.next == None:
            return head
        
        temp = head
        arr = []

        while temp != None:
            arr.append(temp.data)
            temp = temp.next

        arr.sort()

        temp = head
        i = 0

        while temp != None:
            temp.data = arr[i]
            i += 1
            temp = temp.next

        return head
    
    def traversalLL(self,head):
        temp = head

        while temp != None:
            print(temp.data,end=" ")
            temp = temp.next

        print()

        

if __name__ == "__main__":
    head = Node(2)
    second = Node(1)
    third = Node(3)
    fourth = Node(5)
    fifth = Node(6)
    sixth = Node(4)
    seven = Node(7)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = seven

sol = Solution()
startNode =sol.sort_LL(head)
# print(startNode )
sol.traversalLL(head)
