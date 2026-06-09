# Brute Force

'''class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Solution:
    def Remove_NodeK_FromEnd(self,head,k):
        temp = head
        cnt = 0
        while temp != None:
            cnt += 1
            temp = temp.next

        if cnt == k:
            return head.next
        

        temp = head
        res = (cnt-k)

        while temp != None:
            res -= 1

            if res == 0:
                break
            
            temp = temp.next
        delNode = temp.next
        temp.next = temp.next.next
        del delNode
        return head
              
if __name__ == "__main__":
    k = 7
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
startNode = sol.Remove_NodeK_FromEnd(head,k)
temp = startNode

while temp:
    print(temp.data, end=" ")
    temp = temp.next
print()'''

# Optimization Approach

'''class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Solution:
    def Remove_NodeK_FromEnd(self,head,k):
        dummy = Node(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        for _ in range(k+1):
            fast = fast.next

        
        while fast != None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next


              
if __name__ == "__main__":
    k = 2
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
startNode = sol.Remove_NodeK_FromEnd(head,k)
temp = startNode

while temp:
    print(temp.data, end=" ")
    temp = temp.next
print()'''


'''class Solution:
    def Remove_NodeK_FromEnd(self, head, k):

        dummy = Node(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        for _ in range(k + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next'''







