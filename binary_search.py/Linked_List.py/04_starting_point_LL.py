# Brute Force

'''class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Solution:
    def detectCycle(self,head):
        visited = {}
        temp = head

        while temp != None:
            if temp in visited:
                return temp
            
            visited[temp] = 1
            temp = temp.next

        return None
    

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

sol = Solution()
startnode = sol.detectCycle(head)

if startnode:
    print("Cycle starts at node with value",startnode.data)
else:
    print("No Cycle found")'''


# Optimization Approa

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Solution():

    def DetectLoop(self,head):
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = head


                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow
        
        return None
    
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

    fifth.second = fifth
    

sol =  Solution()
startNode =sol.DetectLoop(head)

if startNode:
    print("Staring point of loop Found", startNode.data)

else:
    print("Starting point Not found")

    



