# class Node:
#     def __init__(self,data,next=None):
#         self.data = data
#         self.next = next


# def ConvertArray_LL(arr):
#     head = Node(arr[0])
#     movers = head
#     for i in range(1, len(arr)):
#         temp = Node(arr[i])
#         movers.next = temp
#         movers = temp

#     return head

# def MiddleLL(head):
#     cnt = 0
#     temp = head
#     while temp != None:
#         cnt += 1
#         temp = temp.next

    
#     res = (cnt//2)+1
#     temp = head
#     while temp != None:
#         res -= 1
#         if (res==0):
#             break
#         temp = temp.next

#     return temp.data


# def TraverseLL(head):
#     while head:
#         print(head.data,end=" ")
#         head = head.next

#     print()



# def main():
#     arr = [2,4,6,8,20]
#     head = ConvertArray_LL(arr)
#     TraverseLL(head)
#     length = MiddleLL(head)
#     print(length)

# if __name__ == '__main__':
#     main()

# class Node:
#     def __init__(self,data,next=None):
#         self.data = data
#         self.next = next


# def ConvertArray_LL(arr):
#     head = Node(arr[0])
#     movers = head
#     for i in range(1, len(arr)):
#         temp = Node(arr[i])
#         movers.next = temp
#         movers = temp

#     return head

# def  Reverse_LL(head):
#     if head == None or head.next == None:
#         return None
    
#     temp = head
#     stack = []

#     while temp != None:
#         stack.append(temp.data)
#         temp = temp.next

#     temp = head
#     while temp != None:
#         temp.data = stack.pop()
#         temp = temp.next

#     return head


# def TraverseLL(head):
#     while head:
#         print(head.data,end=" ")
#         head = head.next

#     print()



# def main():
#     arr = [2,4,6,8,20]
#     head = ConvertArray_LL(arr)
#     # TraverseLL(head)
#     length = Reverse_LL(head)
#     # print(length)
#     TraverseLL(head)

# if __name__ == '__main__':
#     main()

'''class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


def ConvertArray_LL(arr):
    head = Node(arr[0])
    movers = head
    for i in range(1, len(arr)):
        temp = Node(arr[i])
        movers.next = temp
        movers = temp

    return head

def  Reverse_LL(head):
    if head == None or head.next == None:
        return None
    
    temp = head
    prev = None

    while temp != None:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front


    return prev
    


def TraverseLL(head):
    while head:
        print(head.data,end=" ")
        head = head.next

    print()



def main():
    arr = [2,4,6,8,20]
    head = ConvertArray_LL(arr)
    # TraverseLL(head)
    head = Reverse_LL(head)
    # print(length)
    TraverseLL(head)

if __name__ == '__main__':
    main()'''

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


class Solution:
    def CheckeLL_in_Loop(self,head):
        visited = []
        temp = head

        while temp != None:
            if temp in visited:
                return True
            
            # visited[temp] = 1
            visited.append(temp)
            temp = temp.next

        return False


if __name__ == '__main__':
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    # fifth.next = second

sol = Solution()
startNode = sol.CheckeLL_in_Loop(head)

if startNode:
    print("Loop is present in linkedList")
else:
    print("Loop is not in linkedList")