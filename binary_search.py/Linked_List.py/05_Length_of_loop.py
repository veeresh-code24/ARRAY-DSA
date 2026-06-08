class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Solution:
    def Lenth_Loop_LL(self,head):
        visited = {}
        count = 1
        temp =  head
        while temp != None:
            if temp in visited:
                return count - visited[temp]


            visited[temp] = count
            count += 1
            temp = temp.next
        
        return 0

if __name__ == "__main__":
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

    sol = Solution()
    length = sol.Lenth_Loop_LL(head)
    print(length)



# Optimization 

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Solution:
    def findLengthLoop(self,slow,fast):

        fast = fast.next
        cnt = 1
        while slow != fast:
            cnt += 1
            fast = fast.next

        return cnt
    
    def lengthOfLoop(self,head):
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return self.findLengthLoop(slow,fast)
            
        
        return 0
if __name__ == "__main__":
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    fourth.next = second


    sol = Solution()
    length = sol.lengthOfLoop(head)
    print(length)


    









