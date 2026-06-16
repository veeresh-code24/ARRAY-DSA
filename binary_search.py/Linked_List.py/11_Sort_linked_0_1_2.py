# Brute Force

'''class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


class Solution:
    def sort_0s_1s_2s(self,head):
        temp = head
        arr = []

        while temp != None:
            arr.append(temp.data)
            temp = temp.next

        arr.sort()

        i = 0
        temp = head
        while temp != None:
            temp.data = arr[i]
            i += 1
            temp = temp.next

        return head
    
    def traverseLL(self,head):
        temp = head

        while temp != None:
            print(temp.data,end=" ")
            temp = temp.next

        print()

if __name__ == "__main__":
    head = Node(0)
    second = Node(1)
    third = Node(1)
    fourth = Node(1)
    fifth = Node(0)
    sixth = Node(2)
    seven = Node(1)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = seven

sol = Solution()
startNode =sol.sort_0s_1s_2s(head)
# print(startNode )
sol.traverseLL(head)'''

# Brute Force 2

'''class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


class Solution:
    def sort_0s_1s_2s(self,head):
        temp = head
        count0,count1,count2 = 0,0,0

        while temp != None:
            if temp.data == 0:
                count0 += 1

            elif temp.data == 1:
                count1 += 1

            else:
                count2 += 1

            temp = temp.next

        temp = head

        while temp != None:
            if count0:
                temp.data = 0
                count0 -= 1

            elif count1:
                temp.data  = 1
                count1 -= 1

            else:
                temp.data = 2
                count2 -= 1

            temp = temp.next

        return head
    
    def traverseLL(self,head):
        temp = head

        while temp != None:
            print(temp.data,end=" ")
            temp = temp.next

        print()

if __name__ == "__main__":
    head = Node(0)
    second = Node(1)
    third = Node(1)
    fourth = Node(1)
    fifth = Node(0)
    sixth = Node(2)
    seven = Node(1)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = seven

sol = Solution()
startNode =sol.sort_0s_1s_2s(head)
# print(startNode )
sol.traverseLL(head)'''

# Optimization

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


class Solution:
    def sort_0s_1s_2s(self,head):
        if head == None or head.next == None:
            return head
        
        zero_dummy = Node(-1)
        one_dummy = Node(-1)
        two_dummy = Node(-1)

        zero_tail = zero_dummy
        one_tail = one_dummy
        two_tail = two_dummy
        temp = head

        while temp != None:
            if temp.data == 0:
                zero_tail.next = temp
                zero_tail = zero_tail.next

            elif temp.data == 1:
                one_tail.next = temp
                one_tail = one_tail.next

            else:
                two_tail.next = temp
                two_tail = two_tail.next

            temp = temp.next

        # connect 0s list to 1s and 2s

        zero_tail.next = one_dummy.next if one_dummy.next else two_dummy.next
        one_tail.next = two_dummy.next
        two_tail.next = None

        # return zero_dummy.next
        return zero_dummy.next or one_dummy.next or two_dummy.next



    
    def traverseLL(self,head):
        temp = head

        while temp != None:
            print(temp.data,end=" ")
            temp = temp.next

        print()

if __name__ == "__main__":
    head = Node(0)
    second = Node(1)
    third = Node(1)
    fourth = Node(1)
    fifth = Node(0)
    sixth = Node(2)
    seven = Node(1)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = seven

sol = Solution()
startNode =sol.sort_0s_1s_2s(head)
# print(startNode )
sol.traverseLL(startNode)