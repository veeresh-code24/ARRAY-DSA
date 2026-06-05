# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None


# #  Traversing Array to LL
# def ConvertArrayLL(arr):
#     head = Node(arr[0])
#     movers = head

#     for i in range(1,len(arr)):
#         temp = Node(arr[i])
#         movers.next = temp

#         movers = temp

#     return head

# # length of LL
# def LengthOfArray(head):
#     count = 0
#     temp = head

#     while temp != None:
#         count += 1

#         temp = temp.next

#     return count

# # Search an element in LL
# def CheckIfPresent(head,val):
#     temp = head

#     while temp != None:
#        if temp.data == val:
#            return 1
       
#        temp = temp.next
       
#     return 0

# def main():

#     arr = [2,4,6,8,9]
#     head = ConvertArrayLL(arr)
#     # print(head.data)
#     # print(LengthOfArray(head))
#     # print(length)
#     present = CheckIfPresent(head,9)
#     print(present)

#     temp = head
#     # Printing LL
#     while temp != None:
#         print(temp.data,end = " ")
#         temp = temp.next

#     print()

# if __name__ == '__main__':
#     main()

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def ConArrayLL(arr):
    head = Node(arr[0])
    movers = head

    for i in range(1,len(arr)):
        temp = Node(arr[i])

        movers.next = temp

        movers = temp

    return head

def traverseArray(head):
    temp = head

    while temp != None:
        print(temp.data, end = " ")

        temp = temp.next

    print()

# def LengthArray(head):
#     temp = head
#     count = 0

#     while temp != None:
#         count += 1

#         temp = temp.next

#     return count

# def checkisPresent(head,val):
#     temp = head
#     while temp != None:
#         if temp.data == val:
#             return temp.data
        
#         temp = temp.next
    
#     return 0

def RemoveHead(head):

    temp = head

    if head == None:
        return head
    
    head = head.next
    del temp

    return head

# def RemoveTail(head):
#     if head == None or head.next == None:
#         return None
    
#     temp = head

#     while temp.next.next != None:
#         temp = temp.next

#     del temp.next
#     temp.next = None

#     return head

# def RemoveKthElement(head,k):
#     if head == None:
#         return None
#     temp = head
#     if k == 1:
#         head = head.next
#         del temp

# def RemoveKthElement(head,k):
#     if head == None:
#         return head
    
#     if k == 1:
#         temp = head
#         head = head.next
#         del temp
#         return head


#     cnt = 0
#     temp = head
#     previous = None

#     while temp != None:
#         cnt += 1

#         if cnt == k:
#             previous.next = temp.next
#             del temp
#             break

#         previous = temp
#         temp = temp.next

#     return head

# def insertHead(head,val):

    # temp = Node(val,head)
    # temp.next = head
    # return temp
    # temp = Node(val)
    # temp.next = head
    # return temp
# def insertTail(head,val):

#     if head == None:
#         return Node(val)
    
#     temp = head

#     while temp.next != None:
#         temp = temp.next

#     temp.next = Node(val)
#     return head

def insertPosition(head,val,k):

    if head == None:
        # temp = Node(val,head)
        return Node(val,head)
    
    if k == 1:
        # temp = Node(val,head)
        return Node(val,head)
    
    cnt = 0
    temp = head
    while temp != None:
        cnt += 1

        if cnt == (k-1):
            x = Node(val,temp.next)
            temp.next = x
            break

        temp = temp.next

    return head
    



def main():
    arr = [2,4,6,8,10]
    head = ConArrayLL(arr)
    # print(head.data)
    # remove =RemoveHead(head)
    # traverseArray(tail)
    # print(remove.data)
    # print(LengthArray(head))
    # print(checkisPresent(head,4))
    # head = RemoveTail(head)
    # print(head)
    # head = RemoveKthElement(head,2)
    # head = insertValue(head,100)
    # head = insertTail(head,100)
    head = insertPosition(head,100,5)
    traverseArray(head)
    

if __name__ == '__main__':
    main()

