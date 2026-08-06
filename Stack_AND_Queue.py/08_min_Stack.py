class Stack:
    def __init__(self, size = 10):
        self.arr = [0] * size
        self.top = -1
        self.capacity = size

    def push(self,x):
        if self.top == self.capacity -1:
            print("Stack Overflow")
            return

        self.top += 1
        self.arr[self.top] = x

    def pop(self):
        if self.top == -1:
            print("Stack id Full")

            return
        

        popped = self.arr[self.top]
        self.top -= 1
        return popped

    def top(self):
        if self.top == -1:
            print("Strack is Full")
            return

        return self.arr[self.top]

    def getMin(self,x):
        if x < self.top:

            return x

if __name__ == '__main__':
    st = Stack()
    commands = ["MinStack","push","push","push","getMin","pop","top","getMin"]
    inputs = [[],[-2],[0],[-3],[],[],[],[]]

    for i in range(len(commands)):
        
            if commands[i] == "push":
                st.push(inputs[i][0])
                print("null", end= " ")
        
            elif commands[i] == 'pop':
                print(st.pop(), end = " ")
        
            elif commands[i] == "top":
                print(st.top(), end= " ")
        
            elif commands[i] == "MinStack":
                print("null", end = " ")

            elif commands[i] == "getMin":
                print(st.getMin(), end = " ")

        
    
    





    



