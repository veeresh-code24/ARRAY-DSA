class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Solution:
    def CheckPalindromeLL(self,head):
        lst = []
        temp = head

        while temp != None:
            lst.append(temp.data)
            temp = temp.next

        if lst == lst[::-1]:
            return True
        else:
            return False


if __name__ == "__main__":
    head = Node(1)
    second = Node(2)
    third = Node(2)
    fourth = Node(3)

    head.next = second
    second.next = third
    third.next = fourth

sol = Solution()
startNode = sol.CheckPalindromeLL(head)

if startNode:
    print("It's Palindrome")
else:
    print("It's not a palindrome")
