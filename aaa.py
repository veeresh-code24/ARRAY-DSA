class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def ArrayTo_LL(arr):
    head = Node(arr[0])
    mover = head

    for i in range(1, len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp

    return head

def LengthOf_LL(head):
    cnt = 0
    temp = head

    while temp != None:
        # cnt += 1

        temp = temp.next
        cnt += 1

    return cnt

def searchIfPresent(head,value):
    if head == None:
        return None
    temp = head
    while temp != None:

        if temp.data == value:
            return 1
        temp = temp.next
        
        
    return 0
    
def DeleteHead(head):
    if head == None:
        return head
    
    head = head.next

    return head

def DeleteTail(head):
    if head == None or head.next == None:
        return None
    
    
    temp = head

    while temp.next.next != None:
        temp = temp.next

    del temp.next 
    temp.next = None
    return head

def deleteKthElement(head,k):
    if head == None:
        return None
    
    if k == 1:
        temp = head
        head = head.next
        del temp
        return head

    
    cnt = 0
    temp = head
    prev = None

    while temp != None:
        cnt += 1

        if cnt == k:
            prev.next = temp.next
            del temp
            break
        
        prev = temp
        temp = temp.next

    return head

def deleteEle(head,value):
    if head == None:
        return None
    
    if head.data == value:
        temp = head
        head = head.next
        del temp
        return head

    
    temp = head
    prev = None

    while temp != None:

        if temp.data == value:
            prev.next = temp.next
            del temp
            break
        
        prev = temp
        temp = temp.next

    return head
    
    
def TraversalArray(head):
    temp = head

    while temp != None:
        print(temp.data, end=" ")

        temp = temp.next

    print()




def main():
    arr = [1,4,6,8]
    head = ArrayTo_LL(arr)
    # print(head.next.next.data
    # length = LengthOf_LL(head)
    # print(length)
    # search = searchIfPresent(head,118)
    # print(search)

    # head = DeleteHead(head)
    # head =  DeleteTail(head)
    # head = deleteKthElement(head,4)
    head = deleteEle(head,1)
    TraversalArray(head)
    # print(head)




if __name__ == '__main__':
    main()
