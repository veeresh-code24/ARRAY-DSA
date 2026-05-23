class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


#  Traversing Array to LL
def ConvertArrayLL(arr):
    head = Node(arr[0])
    movers = head

    for i in range(1,len(arr)):
        temp = Node(arr[i])
        movers.next = temp

        movers = temp

    return head

# length of LL
def LengthOfArray(head):
    count = 0
    temp = head

    while temp != None:
        count += 1

        temp = temp.next

    return count

# Checking present Value
def CheckIfPresent(head,val):
    temp = head

    while temp != None:
       if temp.data == val:
           return 1
       
       temp = temp.next
       
    return 0

def main():

    arr = [2,4,6,8,9]
    head = ConvertArrayLL(arr)
    # print(head.data)
    # print(LengthOfArray(head))
    # print(length)
    present = CheckIfPresent(head,9)
    print(present)

    temp = head
    # Printing LL
    while temp != None:
        print(temp.data,end = " ")
        temp = temp.next

    print()

if __name__ == '__main__':
    main()
