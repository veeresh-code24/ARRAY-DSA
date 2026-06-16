# Brute Force

'''class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Solution:
    def Delete_Middle_node(self,head):
        if head == None or head.next == None:
            return None
        
        temp = head
        cnt = 0

        while temp != None:
            cnt += 1
            temp = temp.next

        res = (cnt//2)

        temp = head
        prev = None

        while temp != None:
            res -= 1

            if res == 0:
                middle = temp.next
                temp.next = temp.next.next
                break
            
            # prev = temp
            # temp = temp.next
            # prev.next = temp.next
            temp.next = temp.next

        # temp.next = temp.next.next
        return head
    

    def TraverLL(self,head):
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
    # seven = Node(7)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    # sixth.next = seven

sol = Solution()
startNode =sol.Delete_Middle_node(head)
print(startNode )
sol.TraverLL(head)'''

# Optimization Approach


class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Solution:
    def Delete_Middle_node(self,head):
        if head == None or head.next == None:
            return head
        
        '''slow = head
        fast = head
        prev = None

        while fast != None and fast.next != None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = prev.next.next
        return head'''

        slow,fast = head,head

        fast = fast.next.next

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return head
            
        

    

    def TraverLL(self,head):
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
    # seven = Node(7)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    # sixth.next = seven

sol = Solution()
startNode =sol.Delete_Middle_node(head)
print(startNode )
sol.TraverLL(head)

