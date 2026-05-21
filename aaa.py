class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def convertArraytoLL(arr):

    head = Node(arr[0])
    movers = head


    for i in range(1,len(arr)):
        temp = Node(arr[i])

        movers.next = temp

        movers = temp

    return head

def LengthofLinkedList(head):
    cnt = 0
    temp = head

    while temp != None:
        cnt += 1

        temp= temp.next

    return cnt

def removeHead(head):
    temp = head

    if head == None:
        return head
    
    head = head.next
    del temp
    return head

def removeTail(head):

    if head == None or head.next == None:
        return None
    

    temp = head

    while temp.next.next != None:
        temp = temp.next

    temp.next = None

    return head

def DeleteK(head,k):
    if head == None:
        return head
    
    if k == 1:
        temp = head
        del temp

        head = head.next
        return head
    cnt = 0
    temp = head
    previous = None

    while temp != None:
        cnt += 1

        if cnt == k:
            previous.next = temp.next
            del temp
            break

        previous = temp
        temp = temp.next

    return head

def main():
    arr = [2,4,6,8]
    k = 4
    head = convertArraytoLL(arr)
    head = DeleteK(head,k)
    

    temp = head

    while temp != None:
        print(temp.data, end = " ")

        temp = temp.next

    print()



if __name__ == '__main__':
    main()

