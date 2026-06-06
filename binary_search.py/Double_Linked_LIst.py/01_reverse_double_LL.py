# Brute Force

class Node:
    def __init__(self,data,next=None,back=None):
        self.data = data
        self.next = next
        self.back = back


def ConvertArray_to_DLL(arr):
    head = Node(arr[0])
    prev = head

    for i in range(1, len(arr)):
        temp = Node(arr[i],None,prev)
        prev.next = temp
        prev = temp

    return head

def reverseDLL(head):
    if head is None:
        return None
    
    stack = []
    temp = head
    while temp is not None:
        stack.append(temp.data)
        temp = temp.next

    temp = head
    while temp is not None:
        temp.data = stack.pop()
        temp = temp.next

    return head

def Traversehead(head):
    temp = head

    while temp is not None:
        print(temp.data, end= " <-> ")
        temp = temp.next

    print("None")


def main():
    arr = [10,20,30,40]
    head = ConvertArray_to_DLL(arr)
    Traversehead(head)  
    head = reverseDLL(head)
    Traversehead(head)

main()


# Optimize Approach

class Node:
    def __init__(self,data,next = None,back=None):
        self.data = data
        self.next = next
        self.back = back

def Con_DD(arr):
    if len(arr) == 0:
        return None
    
    head = Node(arr[0])
    prev = head

    for i in range(1, len(arr)):
        temp = Node(arr[i],None,prev)
        prev.next = temp
        prev = temp

    return head

def reverseDLL(head):

    if head == None or head.next == None:
        return head
    
    current = head
    temp = None

    while current != None:
        temp = current.back
        current.back = current.next
        current.next = temp

        current = current.back

    if temp is not None:
        head = temp.back

    return head

def print_DLL(head):
    
    while head is not None:
        print(head.data, end= " ")
        head = head.next

    print()



def main():
    arr = [2,4,6,8]
    head = Con_DD(arr)
    head = reverseDLL(head)
    print_DLL(head)

main()

