# Brute Force

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


def Con_LL(arr):
    head = Node(arr[0])
    mover = head

    for i in range(1,len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp

    return head

def DetectLoop(head,pos):
    if head == None:
        return False
    
    visited = set()
    temp = head
    while temp != None:
        if temp in visited:
            return True
        
        visited.add(temp)
        temp = temp.next   

    return False
    


def Traverse_LL(head):
    temp = head

    while temp != None:
        print(temp.data,end=" ")
        temp = temp.next

    print()


def main():
    arr = [1,2,3,4,5]
    pos = 1
    head = Con_LL(arr)
    Traverse_LL(head)
    detect = DetectLoop(head,pos)
    print(detect)
    Traverse_LL(head)

main()