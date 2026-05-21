# Array convert into LL. and  traversal Linked List

'''class Node:
    def __init__(self,data):
        self.data = data
        self.next = None



def convertArrayLL(arr):

    head = Node(arr[0])

    mover = head

    for i in range(1,len(arr)):
        temp = Node(arr[i])

        mover.next = temp

        mover = temp

    return head

def main():

    arr = [12,4,6,8,10]

    head = convertArrayLL(arr)

    temp = head

    while temp != None:
        print(temp.data, end = " ")
        temp = temp.next



    # print(head.next.next.next.next.data)

if __name__ == '__main__':
    main()'''


'''   head ─┐
      ↓
temp ─┘
     [12 | • ] → [5 | • ] → [6 | • ] → [8 | None]'''




# LinkedList Length

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


# def convertArrayLL(arr):

    # head = Node(arr[0])
    # mover = head

    # for i in range(1,len(arr)):
        # temp = Node(arr[i])
        # mover.next = temp
        # mover = temp

    # return head

def lengthofLL(head):

    cnt = 0
    temp = head

    while temp != None:
        cnt += 1

        temp = temp.next

    return cnt

def main():
    arr = [2,4,6,8]

    head = convertArrayLL(arr)

    print(lengthofLL(head))

if __name__ == '__main__':
    main()




# Array TO LinkedList

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Convert Array to Linked List
def convertArr2LL(arr):

    head = Node(arr[0])

    mover = head

    for i in range(1, len(arr)):

        temp = Node(arr[i])

        mover.next = temp

        mover = temp

    return head


# Print Linked List
def printLL(head):

    while head != None:

        print(head.data, end=" ")

        head = head.next

    print()


# Remove Head Node
def removeHead(head):

    # If linked list is empty
    if head == None:
        return head

    # Temporary node
    temp = head

    # Move head to next node
    head = head.next

    # Delete old head
    del temp

    return head


# Main Function
def main():

    arr = [12, 5, 8, 7]

    head = convertArr2LL(arr)

    print("Before removing head:")
    printLL(head)

    head = removeHead(head)

    print("After removing head:")
    printLL(head)


if __name__ == '__main__':
    main()

'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Convert Array to Linked List
def convertArr2LL(arr):

    head = Node(arr[0])

    mover = head

    for i in range(1, len(arr)):

        temp = Node(arr[i])

        mover.next = temp

        mover = temp

    return head


# Print Linked List
def printLL(head):

    while head != None:

        print(head.data, end=" ")

        head = head.next

    print()


# Remove Tail Node
def removeTail(head):

    # Empty linked list OR single node
    if head == None or head.next == None:
        return None

    temp = head

    # Stop at second last node
    while temp.next.next != None:

        temp = temp.next

    # Remove last node
    temp.next = None

    return head


# Main
def main():

    arr = [12, 5, 6, 8]

    head = convertArr2LL(arr)

    print("Before removing tail:")
    printLL(head)

    head = removeTail(head)

    print("After removing tail:")
    printLL(head)


if __name__ == '__main__':
    main()'''



'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Convert Array to Linked List
def convertArr2LL(arr):

    head = Node(arr[0])

    mover = head

    for i in range(1, len(arr)):

        temp = Node(arr[i])

        mover.next = temp

        mover = temp

    return head


# Print Linked List
def printLL(head):

    temp = head

    while temp != None:

        print(temp.data, end=" ")

        temp = temp.next

    print()


# Delete Kth Node
def removeK(head, k):

    # Empty linked list
    if head == None:
        return head

    # Delete first node
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

        # Found kth node
        if cnt == k:

            prev.next = temp.next

            del temp

            break

        prev = temp

        temp = temp.next

    return head


# Main Function
def main():

    arr = [12, 5, 8, 7]

    head = convertArr2LL(arr)

    print("Before deleting kth node:")
    printLL(head)

    k = 3

    head = removeK(head, k)

    print("After deleting kth node:")
    printLL(head)


if __name__ == '__main__':
    main()'''