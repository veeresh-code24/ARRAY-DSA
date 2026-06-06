# class Node:
#     def __init__(self,data,next=None):
#         self.data = data
#         self.next = next

# def ArrayTo_LL(arr):
#     head = Node(arr[0])
#     mover = head

#     for i in range(1, len(arr)):
#         temp = Node(arr[i])
#         mover.next = temp
#         mover = temp

#     return head

# def LengthOf_LL(head):
#     cnt = 0
#     temp = head

#     while temp != None:
#         # cnt += 1

#         temp = temp.next
#         cnt += 1

#     return cnt

# def searchIfPresent(head,value):
#     if head == None:
#         return None
#     temp = head
#     while temp != None:

#         if temp.data == value:
#             return 1
#         temp = temp.next
        
        
#     return 0
    
# def DeleteHead(head):
#     if head == None:
#         return head
    
#     head = head.next

#     return head

# def DeleteTail(head):
#     if head == None or head.next == None:
#         return None
    
    
#     temp = head

#     while temp.next.next != None:
#         temp = temp.next

#     del temp.next 
#     temp.next = None
#     return head

# def deleteKthElement(head,k):
#     if head == None:
#         return None
    
#     if k == 1:
#         temp = head
#         head = head.next
#         del temp
#         return head

    
#     cnt = 0
#     temp = head
#     prev = None

#     while temp != None:
#         cnt += 1

#         if cnt == k:
#             prev.next = temp.next
#             del temp
#             break
        
#         prev = temp
#         temp = temp.next

#     return head

# def deleteEle(head,value):
#     if head == None:
#         return None
    
#     if head.data == value:
#         temp = head
#         head = head.next
#         del temp
#         return head

    
#     temp = head
#     prev = None

#     while temp != None:

#         if temp.data == value:
#             prev.next = temp.next
#             del temp
#             break
        
#         prev = temp
#         temp = temp.next

#     return head

# def Ins_Head(head,value):
#     if head == None:
#         return Node(value)
    
#     temp = Node(value)
#     temp.next = head

#     return temp

# def Ins_Tail(head,value):
#     if head == None:
#         return Node(value)
    
#     temp = head

#     while temp.next != None:

#         temp = temp.next

#     temp.next = Node(value)
#     temp = temp.next
#     del temp

#     return head

# def insertKthValue(head,value,k):
#     if head == None:
#         if k == 1:
#             return Node(value)
        
#         else:
#             return None
        
#     if k == 1:
#         return Node(value,head)
        
#     cnt = 0
#     temp = head

#     while temp != None:
#         cnt += 1
#         if cnt == (k-1):
#             x = Node(value,temp.next)
#             temp.next = x
#             break

#         temp = temp.next

#     return head


 
# def TraversalArray(head):
#     temp = head

#     while temp != None:
#         print(temp.data, end=" ")

#         temp = temp.next

#     print()




# def main():
#     arr = [1,4,6,8]
#     head = ArrayTo_LL(arr)
#     # print(head.next.next.data
#     # length = LengthOf_LL(head)
#     # print(length)
#     # search = searchIfPresent(head,118)
#     # print(search)

#     # head = DeleteHead(head)
#     # head =  DeleteTail(head)
#     # head = deleteKthElement(head,4)
#     # head = deleteEle(head,1)
#     # head = Ins_Head(head,5)
#     # Ins_Tail(head,10)
#     head = insertKthValue(head,100,1)
#     TraversalArray(head)
#     # print(head)




# if __name__ == '__main__':
#     main()

class Node:
    def __init__(self,data,next=None,back=None):
        self.data = data
        self.next = next
        self.back = back

def ConvertArr_DLL(arr):
    head = Node(arr[0])
    prev = head

    for i in range(1,len(arr)):
        temp = Node(arr[i],None,prev)
        prev.next = temp
        prev = temp

    return head

def DeleteHead(head):
    if head == None or head.next == None:
        return None
    
    temp = head
    head = head.next
    head.back = None
    temp.next = None
    del temp
    return head

def Traverse_DLL(head):
    temp = head
    while temp != None:
        print(temp.data,end= " ")
        temp = temp.next

    print()

def DeleteTail(head):
    if head == None or head.next == None:
        return None
    
    temp = head

    while temp.next != None:
        temp = temp.next

    prev = temp.back
    prev.next = None
    temp.back = None

    return head

def DeleteKthElement(head,k):
    if head == None:
        return None
    
    if k == 1:
        return DeleteHead(head)
    
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
    
    prev.next = temp.next
    front.back = prev

    temp.next = None
    temp.back = None

    return head

def DeleteNode(temp):
    prev = temp.back
    front = temp.next

    if front == None:
        prev.next = None
        temp.back = None
        del temp
        return 
    
    prev.next = front
    front.back = prev

    temp.next = None
    temp.back = None
    del temp

def Inserthead(head,value):
    if head == None:
        return Node(value)
    
    # temp = Node(value)
    # temp.next = head
    # head.back = temp
    # return temp

    new_Node = Node(value,head,None)
    head.back = new_Node

    return new_Node

def InsertTailAfter(head,value):
    if head == None:
        return Node(value)
    
    temp = head
    while temp.next != None:
        temp = temp.next

    newNode = Node(value,None,temp)
    temp.next = newNode

    return head

def InsertTailBefore(head,value):
    if head == None:
        return None
    
    tail = head

    while tail.next != None:
        tail = tail.next
    
    prev = tail.back
    newNode = Node(value,tail,prev)
    prev.next = newNode
    tail.back = newNode

    return head


    
def main():
    arr = [5,12,87,7]
    head = ConvertArr_DLL(arr)
    # print(head.data)
    # head = DeleteHead(head)
    # head = DeleteTail(head)
    # head = DeleteKthElement(head,4)
    # DeleteNode(head.next)
    # head = Inserthead(head,2)
    head = InsertTailBefore(head,1000000)
    Traverse_DLL(head)


if __name__ == '__main__':
    main()


