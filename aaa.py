'''class StackArray:
    def __init__(self, size = 10):
        self.arr = [0] * size
        self.top = -1
        self.capacity = size


    def push(self, x):
        if self.top == self.capacity - 1:
            print("Srack overflow")
            return

        self.top += 1
        self.arr[self.top] = x

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty: ")
            return -1

        popped = self.arr[self.top]
        self.top -= 1
        return popped

    def peek(self):
        if self.isEmpty():
            print("Stack is Empty: ")
            return -1

        return self.arr[self.top]

    def isEmpty(self):
        return self.top == -1


if __name__ == '__main__':
    st = StackArray()
    commands = ["StackArray", "push","push", "peek", "pop", "isEmpty"]
    inputs = [[], [5], [10], [], [], []]

    for i in range(len(commands)):
        if commands[i] == "push":
            st.push(inputs[i][0])
            print("null", end = " ")

        elif commands[i] == "pop":
            print(st.pop(), end = " ")

        elif commands[i] == "peek":
            print(st.peek(), end = " ")

        elif commands[i] == "isEmpty":
            print("true" if st.isEmpty() else "false", end = " ")

        elif commands[i] == "StackArray":
            print("null", end =" ")

'''

'''class QueueArray:

    def __init__(self):
        self.arr = [0] * 1
        self.start = -1
        self.end = -1
        self.currSize = 0
        self.maxSize = 1


    def push(self, x):
        if self.currSize == self.maxSize:
            print("Queue is Full")
            exit(1)

        if self.end == -1:
            self.start += 1
            self.end += 1

        else:
            self.end = (self.end + 1) % self.maxSize

        self.arr[self.end] = x
        self.currSize += 1


    def pop(self):
        if self.start == -1:
            print("Queue is Empty")
            exit(1)

        popped = self.arr[self.start]

        if self.currSize == 1:
            self.start -= 1
            self.end -= 1

        else:
            self.start = (self.start + 1 ) % self.maxSize

        self.currSize -= 1
        return popped

    def peek(self):
        if self.start == -1:
            print("Queue is Empty")
            exit(1)

        return self.arr[self.start]

    def isEmpty(self):
        return self.currSize == 0

if __name__ == '__main__':
    st = QueueArray()
    commands = ["push", "push","push", "peek", "pop", "isEmpty"]
    inputs = [[5], [5], [10], [], [], []]

    for i in range(len(commands)):
        if commands[i] == "push":
            st.push(inputs[i][0])
            print("null", end = " ")

        elif commands[i] == "pop":
            print(st.pop(), end = " ")

        elif commands[i] == "peek":
            print(st.peek(), end = " ")

        elif commands[i] == "isEmpty":
            print("true" if st.isEmpty() else "false", end = " ")

        elif commands[i] == "StackArray":
            print("null", end =" ")






'''


class Node:
    def __init__(self, d):
        self.val = d
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, x):

        element = Node(x)
        element.next = self.head
        self.head = element


    def pop(self):
        if self.head is None:
            return -1
        temp = self.head.val

        self.head = self.head.next

        return temp

    def peek(self):
        if self.head is None:
            return -1

        return self.head.val

    def isEmpty(self):
        return self.head == None

if __name__ == '__main__':
    st = LinkedList()
    commands = ["push", "push","push", "peek", "pop", "isEmpty"]
    inputs = [[5], [5], [10], [], [], []]

    for i in range(len(commands)):
        if commands[i] == "push":
            st.push(inputs[i][0])
            print("null", end = " ")

        elif commands[i] == "pop":
            print(st.pop(), end = " ")

        elif commands[i] == "peek":
            print(st.peek(), end = " ")

        elif commands[i] == "isEmpty":
            print("true" if st.isEmpty() else "false", end = " ")

        elif commands[i] == "StackArray":
            print("null", end =" ")


    
    




