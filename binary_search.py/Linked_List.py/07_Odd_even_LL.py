# Brute Force

'''class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


class Solution:
    def Odd_Even_LL(self,head):

        temp = head
        lst = []
        while temp != None and temp.next != None:
            lst.append(temp.data)
            temp = temp.next.next

        if temp:
            lst.append(temp.data)

        temp = head.next
        while temp != None and temp.next != None:
            lst.append(temp.data)
            temp = temp.next.next

        if temp:
            lst.append(temp.data)

        i = 0
        temp = head

        while temp != None:
            temp.data = lst[i]
            i += 1
            temp = temp.next

        return head






if __name__ == "__main__":
    head = Node(2)
    second = Node(1)
    third = Node(3)
    fourth = Node(5)
    fifth = Node(6)
    sixth = Node(4)
    seven = Node(7)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = seven

sol = Solution()
startNode = sol.Odd_Even_LL(head)

temp = startNode
while temp != None:
    print(temp.data, end=" ")
    temp = temp.next'''

# Brute Solution

'''class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


class Solution:
    def Odd_even_LL(self,head):

        temp = head
        pos = 1
        odd = []
        even = []

        while temp != None:
            if pos % 2 == 1:
                odd.append(temp)

            else:
                even.append(temp)

            pos += 1
            temp = temp.next

        lst = []
        for Node in odd:
            lst.append(Node)

        for Node in even:
            lst.append(Node)


        head = lst[0]
        movers = head

        for i in range(1,len(lst)):
            temp = lst[i]
            movers.next = temp
            movers = temp

        movers.next = None
        return head


if __name__ == "__main__":
    head = Node(2)
    second = Node(1)
    third = Node(3)
    fourth = Node(5)
    fifth = Node(6)
    sixth = Node(4)
    seven = Node(7)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = seven

sol = Solution()
startNode = sol.Odd_even_LL(head)
temp = startNode

while temp != None:
    print(temp.data, end=" ")
    temp = temp.next
# print(startNode)'''


# Optimization Approach

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = None


class Solution:
    def Odd_Even_LL(self,head):

        odd = head
        even = head.next
        evenhead = even

        while even != None and even.next != None:
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next

        odd.next = evenhead

        return head



if __name__ == "__main__":

    head = Node(2)
    second = Node(1)
    third = Node(3)
    fourth = Node(5)
    fifth = Node(6)
    sixth = Node(4)
    seven = Node(7)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = seven

sol = Solution()
startNode = sol.Odd_Even_LL(head)

temp = startNode

while temp:
    print(temp.data,end = " ")
    temp = temp.next

print()







