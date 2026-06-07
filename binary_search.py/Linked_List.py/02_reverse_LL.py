# Brute Force
'''class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


def Con_LL(arr):
    head = Node(arr[0])
    mover = head

    for i in range(1,len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp

    return head

def Reverse_LL(head):

    stack = []
    temp = head
    while temp != None:
        stack.append(temp.data)
        temp = temp.next

    temp = head
    while temp != None:
        temp.data = stack.pop()
        temp = temp.next

    return head

def Traverse_LL(head):
    temp = head

    while temp != None:
        print(temp.data,end=" ")
        temp = temp.next

    print()


def main():
    arr = [2,4,6,8,10,12]
    head = Con_LL(arr)
    Traverse_LL(head)
    head = Reverse_LL(head)
    Traverse_LL(head)

main()'''


# Optimization


class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


def Con_LL(arr):
    head = Node(arr[0])
    mover = head

    for i in range(1,len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp

    return head

def Reverse_LL(head):
    if head == None or head.next == None:
        return head
    
    temp = head
    prev = None

    while temp != None:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front

    return prev
    


def Traverse_LL(head):
    temp = head

    while temp != None:
        print(temp.data,end=" ")
        temp = temp.next

    print()


def main():
    arr = [2,4,6,8,10,12]
    head = Con_LL(arr)
    Traverse_LL(head)
    head = Reverse_LL(head)
    Traverse_LL(head)

main()

