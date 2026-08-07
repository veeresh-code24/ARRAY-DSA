class MinStack:
    def __init__(self):
        self.st = []

    def push(self,val):

        if not self.st:
            self.st.append((val, val))
            return


        mini = min(self.getMin(), val)

        self.st.append((val, mini))

    def pop(self):
        return self.st.pop()

    def top(self):
        return self.st[-1][0]

    def getMin(self):
        return self.st[-1][1]

if __name__ == "__main__":
    s = MinStack()
    
    # Function calls
    s.push(-2)
    s.push(0)
    s.push(-3)
    print(s.getMin(), end=" ")
    s.pop()
    print(s.top(), end=" ")
    s.pop()
    print(s.getMin())

