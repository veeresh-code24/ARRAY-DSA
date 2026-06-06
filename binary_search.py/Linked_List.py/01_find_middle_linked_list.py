# Brute Force

'''class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def ConverTo_LL(arr):

    head = Node(arr[0])
    mover = head

    for i in range(1, len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover  = temp

    return head

def lengthLL(head):
    temp = head
    
    cnt = 0
    while temp != None:
        cnt += 1
        temp = temp.next

    
    # n = (cnt//2)+1
    # temp = head
    # cnt = 0
    # while temp != None:
    #     cnt += 1

    #     if cnt == n:

    #         return temp.data
        
    #     temp = temp.next

    middleNode = (cnt//2)+1

    temp = head

    while temp != None:
        middleNode -= 1

        if middleNode == 0:
            break
        temp = temp.next

    return temp.data
        


def TraverLL(head):
    temp = head
    while temp != None:
        print(temp.data,end=" ")
        temp = temp.next

    print()



def main():
    arr = [2,4,6,8,11,13,10]
    head =  ConverTo_LL(arr)
    # head = 
    TraverLL(head)
    length = lengthLL(head)
    print(length)

main()'''

# Optimization

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def ConLL(arr):
    head = Node(arr[0])
    mover = head

    for i in range(1, len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp

    return head

def findMiddle_Node(head):
    slow = head
    fast = head

    while fast != None and fast.next != None:

        slow = slow.next
        fast = fast.next.next

    return slow.data

def Traverse_LL(head):
    temp = head

    while temp != None:
        print(temp.data,end=" ")
        temp = temp.next

    print()



def main():
    arr = [2,4,6,8,10]
    head = ConLL(arr)
    answer = findMiddle_Node(head)
    print(answer)
    Traverse_LL(head)

main()
    

