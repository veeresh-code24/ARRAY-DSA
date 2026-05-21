class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def TraverseArray(arr):
    head = Node(arr[0])
    movers = head

    for i in range(1,len(arr)):
        temp = Node(arr[i])
        movers.next = temp
        movers = temp

    return head

def PrintLL(head):
    temp = head

    while temp != None:
        print(temp.data, end=" ")

        temp = temp.next

    # print()


def main():
    arr = [2,5,8,6]

    head = TraverseArray(arr)
    print(head.data)

    head = PrintLL(head)

if __name__ == '__main__':
    main()


