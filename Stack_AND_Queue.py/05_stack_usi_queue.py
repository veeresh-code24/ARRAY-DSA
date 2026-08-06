from queue import Queue

class QueueStack:
    def __init__(self):
        self.q = Queue()


    def push(self, x):

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


if __name__ == '__main__':
    st = QueueStack()

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







