class Node:
    def __init__(self,d):
        self.val = d
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.start = self.end = None
        self.size = 0


    def push(self, x):

        element = Node(x)

        if self.start == None:
            self.start = self.end = element

        else:
            self.end.next  = element
            self.end = element

        self.size += 1


    def pop(self):
        if self.start is None:
            return -1

        value = self.start.val
        self.start = self.start.next
        self.size -= 1

        if self.start is None:
            self.end = None

        return value


    def peek(self):
        if self.start == None:
            return -1

        return self.start.val


    def isEmpty(self):
        return self.size == 0


if __name__ == '__main__':
    st = LinkedListQueue()

    commands = ["ArrayQueue", "push", "push", "peek", "pop", "isEmpty"]
    inputs = [[], [5], [10], [], [],[] ]
    
    for i in range(len(commands)):
    
        if commands[i] == "push":
            st.push(inputs[i][0])
            print("null", end= " ")
    
        elif commands[i] == 'pop':
            print(st.pop(), end = " ")
    
        elif commands[i] == "peek":
            print(st.peek(), end= " ")
    
        elif commands[i] == "isEmpty":
            print("true" if st.isEmpty() else "false")
    
        elif commands[i] == "ArrayQueue":
            print("null", end = " ")



