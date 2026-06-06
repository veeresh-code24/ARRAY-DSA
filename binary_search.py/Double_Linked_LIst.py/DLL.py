class Node:
    def __init__(self,data,next=None,back=None):
        self.data = data
        self.next = next
        self.back = back
# Convert TO LL
def  Traverse__Arr_to_LL(arr):
    head = Node(arr[0])
    prev = head

    for i in range(1, len(arr)):
        temp = Node(arr[i])
        prev.next = temp
        temp.back = prev

        prev = temp

    return head

# Delete Head
def DeleteHead(head):
    if head == None or head.next == None:
        return None
    
    prev = head
    head = head.next

    head.back = None
    prev.next = None
    del prev

    return head

# Delete Tail
def DeleteTail(head):
    if head == None or head.next == None:
        return None
  
    tail = head

    while tail.next != None:
        tail = tail.next
    
    prev = tail.back

    prev.next = None
    tail.back = None
    del tail

    return head

# Delete Kth Element

def deleteKthElement(head,k):
    # if head == None:
    #     return None
    
    # cnt = 0
    # temp = head

    # while temp!= None:
    #     cnt += 1

    #     if cnt == k:
    #         break
    #     temp = temp.next
    
    # if temp == None:   # k greater than length
    #     return head
    
    # prev = temp.back
    # front = temp.next

    # #  Only one node in DLL
    # if prev == None and front == None:
    #     return None
    
    # # Delete head
    # elif prev == None:
    #     return DeleteHead(head)
    
    # # Delete tail
    # elif front == None:
    #     return  DeleteTail(head)
    
    # # Delete Middle Node
    # prev.next = front
    # front.back = prev

    # temp.next = None
    # temp.back = None

    # return head

    if head == None:
        return None
    
    temp = head
    cnt = 0

    while temp != None:
        cnt += 1

        if cnt == k:
            break
        temp = temp.next

    if temp == None:
        return head
    
    prev = temp.back
    front = temp.next

    if prev == None and front == None:
        return None
    
    elif prev == None:
        return DeleteHead(head)

    
    elif front == None:
        return DeleteTail(head)
    
    prev.next = front
    front.back = prev

    temp.next = None
    temp.back = None

    return head

          
# Traversing Array
def Travel_LL(head):
    while head:
        print(head.data, end= " ")
        head = head.next

    print()

def main():
    arr = [12,5,8,7]
    head = Traverse__Arr_to_LL(arr)
    print(head.next.data)
    # head = Travel_LL(head)
    # head = DeleteHead(head)
    # head = DeleteTail(head)
    head = deleteKthElement(head,1)
    head = Travel_LL(head)

if __name__ == '__main__':
    main()


