class Node:
    def __init__(self, d):
        self.val = d
        self.next = None


class LinkedListStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, x):

        element = Node(x)

        element.next = self.head
        self.head = element

        self.size += 1


    def pop(self):
        if self.head is None:
            return -1

        value = self.head.val
        self.head = self.head.next

        return value


    def top(self):
        if self.head is None:
            return -1

        return self.head.val

    def isEmpty(self):
        return self.size == 0


if __name__ == '__main__':
    st = LinkedListStack()

    commands = ["ArrayQueue", "push", "push", "top", "pop", "isEmpty"]
    inputs = [[], [5], [10], [], [],[] ]
    
    for i in range(len(commands)):
    
        if commands[i] == "push":
            st.push(inputs[i][0])
            print("null", end= " ")
    
        elif commands[i] == 'pop':
            print(st.pop(), end = " ")
    
        elif commands[i] == "top":
            print(st.top(), end= " ")
    
        elif commands[i] == "isEmpty":
            print("true" if st.isEmpty() else "false")
    
        elif commands[i] == "ArrayQueue":
            print("null", end = " ")


    

