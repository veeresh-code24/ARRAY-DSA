# Converting Stack using Array

'''class ArrayStack:
    def __init__(self,size=1000):
        self.stackArray = [0] * size
        self.capacity = size
        self.topIndex = -1



    def push(self,x):
        if self.topIndex >= self.capacity -1:
            print("Stack OverFlow")
            return
        
        self.topIndex += 1
        self.stackArray[self.topIndex] = x


    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return -1
        
        top_element = self.stackArray[self.topIndex]
        self.topIndex -= 1
        return top_element
    
    def top(self):
        if self.isEmpty():
            print(" is Empty")
            return -1
        return self.stackArray[self.topIndex]
    
    def isEmpty(self):
        return self.topIndex == -1
    

if __name__ == "__main__":
    stack = ArrayStack()
    # commands = ["ArrayStack", "push","push", "top", "pop", "isEmpty"]
    commands = ["pop","pop"]
    inputs = [[], [5], [10], [],[],[]]

    for i in range(len(commands)):
        if commands[i] == "push":
            stack.push(inputs[i][0])
            print("null", end=" ")

        elif commands[i] == "pop":
            print(stack.pop(), end=" ")

        elif commands[i] == "top":
            print(stack.top(), end= " ")

        elif commands[i] == "isEmpty":
            print("true" if stack.isEmpty() else "false", end= " ")

        elif commands[i] == "ArrayStack":
            print("null", end = " ")'''


# Converting Queue using Array

'''class ArrayQueue:
    def __init__(self):
        self.arr = [0] * 10
        self.start = -1
        self.end = -1

        self.currsize = 0
        self.maxsize = 10

    def push(self,x):
        if self.currsize == self.maxsize:
            print("Queue is Full")
            exit(1)

        if self.end == -1:
            self.start = 0
            self.end = 0

        else:
            self.end = (self.end+1)%self.maxsize

        self.arr[self.end] = x
        self.currsize += 1

    def pop(self):
        if self.start == -1:
            print("Queue is Empty")
            exit(1)

        popped = self.arr[self.start]

        if self.currsize == 1:
            self.start = -1
            self.end =  -1

        else:
            self.start = (self.start+1)%self.maxsize

        self.currsize -= 1
        return popped
    
    def peek(self):
        if self.start == -1:
            print("Queue is Empty")
            exit(1)

        return self.arr[self.start]
    
    def isEmpty(self):
        return self.currsize == 0
    

if __name__ == "__main__":
    queue = ArrayQueue()
    commands = ["ArrayQueue","push","push","peek","pop","isEmpty"]
    inputs = [[],[5],[10],[],[],[]]

    for i in range(len(commands)):
        if commands[i] == "push":
            queue.push(inputs[i][0])
            print("null",end= " ")

        elif commands[i] == "pop":
            print(queue.pop(), end=" ")

        elif commands[i] == "peek":
            print(queue.peek(), end= " ")

        elif commands[i] == "isEmpty":
            print("true" if queue.isEmpty() else "false")

        elif commands[i] == "ArrayQueue":
            print("null", end= " ")'''

# Converting Stack using Queue

'''class ArrayQueue:
    def __init__(self):
        self.arr = [0] * 10
        
        self.start = -1
        self.end = -1

        self.currsize = 0
        self.maxsize = 10


    def push(self,x):
        if self.currsize == self.maxsize:
            print("Queue is Full")
            exit(1)

        if self.end == -1:
            self.start = 0
            self.end = 0

        else:
            self.end = (self.end+1) % self.maxsize

        self.arr[self.end] = x
        self.currsize += 1

    def pop(self):
        if self.start == -1:
            print("Queue is Empty")
            exit(1)

        popped = self.arr[self.start]
        if self.currsize == 1:
            self.start = -1
            self.end = -1

        else:
            self.start = (self.start+1) % self.maxsize

        self.currsize -= 1
        return popped
    
    def peek(self):
        if self.start  == -1:
            print("Queue is Empty")

        return self.arr[self.start]
    
    def isEmpty(self):
        return self.currsize == 0
    

if __name__ == "__main__":
    queue = ArrayQueue()
    commands = ["ArrayStack", "push", "push", "pop","peek","isEmpty"]
    inputs = [[],[5],[10],[],[],[]]

    for i in range(len(commands)):
        if commands[i] == "push":
            queue.push(inputs[i][0])
            print("null", end=" ")

        elif commands[i] == "pop":
            print(queue.pop(), end=" ")

        elif commands[i] == "peek":
            print(queue.peek(), end=" ")

        elif commands[i] == "ArrayStack":
            print("null", end=" ")

        elif commands[i] == "isEmpty":
            print("true" if queue.isEmpty() else "false")'''

# Converting Stack using LinkedList

'''class Node:
    def __init__(self,d):
        self.val = d
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self,x):
        element = Node(x)

        element.next = self.head
        self.head = element

        self.size += 1

    def pop(self):
        if self.head == None:
            return -1
        
        value = self.head.val
        temp = self.head
        self.head = self.head.next
        del temp
        self.size -= 1

        return value
    
    def top(self):
        if self.head is None:
            return -1
        
        return self.head.val
    
    def isEmpty(self):
        return self.size == 0
    
st = LinkedListStack()

# List of commands
commands = ["LinkedListStack", "push", "push", "pop", "top", "isEmpty"]
# List of inputs
inputs = [[], [3], [7], [], [], []]

for i in range(len(commands)):
    if commands[i] == "push":
        st.push(inputs[i][0])
        print("null", end=" ")
    elif commands[i] == "pop":
        print(st.pop(), end=" ")
    elif commands[i] == "top":
        print(st.top(), end=" ")
    elif commands[i] == "isEmpty":
        print("true" if st.isEmpty() else "false", end=" ")
    elif commands[i] == "LinkedListStack":
        print("null", end=" ")'''


'''class Node:
    def __init__(self,d):
        self.val = d
        self.next = None


class LinkedListStack:
    def __init__(self):
        self.head = None
        self.stack_size = 0

    def push(self,x):
        element = Node(x)

        element.next = self.head
        self.head = element

        self.stack_size += 1

    def pop(self):
        if self.head == None:
            return -1
        
        value = self.head.val
        temp = self.head
        self.head = self.head.next
        del temp

        self.stack_size -= 1
        return value
    
    def top(self):
        if self.head == None:
            return -1
        
        return self.head.val
    
    def size(self):
        return self.stack_size
    
    def isEmpty(self):
        return self.stack_size == 0
    

st = LinkedListStack()


commands = ["ArrayStack","push","push","pop","top","size","isEmpty"]
inputs = [[],[10],[8],[],[],[],[]]

for i in range(len(commands)):
    if commands[i] == "push":
        st.push(inputs[i][0])
        print("null", end=" ")

    elif commands[i] == "pop":
        print(st.pop(),end= " ")

    elif commands[i] == "top":
        print(st.top(), end=" ")

    elif commands[i] == "size":
        print(st.size(), end= " ")

    elif commands[i] == "isEmpty":
        print("true" if st.isEmpty() else "false",end= " ")

    elif commands[i] == "ArrayStack":
        print("null", end= " ")'''

# Implement Queue using Linkedlist

'''class Node:
    def __init__(self,d):
        self.val = d
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.start = self.end = None
        self.size = 0


    def push(self,x):
        element = Node(x)

        if self.start == None:
            self.start = self.end = element

        else:
            self.end.next = element
            self.end = element

        self.size += 1

    def pop(self):
        if self.start == None:
            return -1
        
        value = self.start.val
        temp = self.start
        self.start = self.start.start
        del temp

        self.size -= 1
        return value
    
    def peek(self):
        if self.start == None:
            return -1
        
        return self.start.val
    
    def Size(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
q = '''

# Implement Stack Using Queue

'''from queue import Queue

class QueueStack:
    def __init__(self):
        self.q = Queue()

    def push(self,x):
        s = self.q.qsize()

        self.q.put(x)

        for _ in range(s):
            self.q.put(self.q.get())

    def pop(self):
        n = self.q.queue[0]
        self.q.get()
        return n
    
    def top(self):
        return self.q.queue[0]
    
    def isEmpty(self):
        return self.q.empty()
    
if __name__ == "__main__":
    st = QueueStack()

    commands = ["QueueStack","push","push","pop","top","isEmpty"]
    inputs = [[],[4],[8],[],[],[]]

    for i in range(len(commands)):
        if commands[i] == "push":
            st.push(inputs[[i][0]])
            print("null", end=" ")

        elif commands[i] == "pop":
            print(st.pop(), end=" ")

        elif commands[i] == "top":
            print(st.top(), end=" ")

        elif commands[i] == "isEmpty":
            print("true" if st.isEmpty() else "false")

        elif commands[i] == "QueueStack":
            print("null", end=" ")'''


from queue import Queue

class QueueStack:
    def __init__(self):
        self.q = Queue()

    def push(self,x):
        s = self.q.qsize()

        self.q.put(x)

        for _ in range(s):
            self.q.put(self.q.get())

    def pop(self):
        n = self.q.queue[0]
        self.q.get()
        return n
    
    def top(self):
        return self.q.queue[0]
    
    def Size(self):
        return self.q.qsize()
    
    def isEmpty(self):
        return self.q.empty()
    

if __name__ == "__main__":
    st = QueueStack()
    commands = ["QueueStack","push", "push","pop","top","isEmpty","Size"]
    inputs = [[],[4],[8],[],[],[],[]]

    for i in range(len(commands)):
        if commands[i] == "push":
            st.push(inputs[i][0])
            print("null", end=" ")

        elif commands[i] == "pop":
            print(st.pop(), end=" ")

        elif commands[i] == "top":
            print(st.top(),end=" " )

        elif commands[i] == "isEmpty":
            print("true" if st.isEmpty() else "false" ,end=" ")

        elif commands[i] == "Size":
            print(st.Size(), end=" ")

        elif commands[i] == "QueueStack":
            print("null", end=" ")


            












        