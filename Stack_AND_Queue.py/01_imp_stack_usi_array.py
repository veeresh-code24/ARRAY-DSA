'''class ArrayStack:

    def __init__(self, size=1):
        self.stackArray = [0] * size
        self.capacity = size
        self.topIndex = -1


    def push(self, x):
        if self.topIndex >= self.capacity -1:
            print('Stack OverFlow')
            return

        self.topIndex += 1
        self.stackArray[self.topIndex] = x


    def pop(self):
        if self.isEmpty():
            print('Stack is empty')
            return -1

        top_element = self.stackArray[self.topIndex]
        self.topIndex -= 1
        return top_element

    def top(self):
        if self.isEmpty():
            print("Stack is Empty")
            return -1

        return self.stackArray[self.topIndex]

    def isEmpty(self):
        return self.topIndex == -1


if __name__ == '__main__':
    stack = ArrayStack()
    commands = ["ArrayStack", "push", "push", "top", "pop", "isEmpty"]
    inputs = [[], [5], [10], [], [], []]

    for i in range(len(commands)):
        if commands[i] == "push":
            stack.push(inputs[i][0])
            print("null", end=" ")

        elif commands[i] == "pop":
            print(stack.pop(), end = " ")

        elif commands[i] == "top":
            print(stack.top(), end = " ")

        elif commands[i] == "isEmpty":
            print("true" if stack.isEmpty() else "False")

        elif commands[i] == "ArrayStack":
            print("null", end= " ")'''


class ArrayStack:

    def __init__(self, size = 1000):
        self.StackArray = [0] * size
        self.capacity = size
        self.topIndex = -1


    def push(self, x):
        if self.topIndex == self.capacity -1:
            print("Stack OverFlow")
            return

        self.topIndex += 1
        self.StackArray[self.topIndex] = x


    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return -1

        top_element = self.StackArray[self.topIndex]
        self.topIndex -= 1
        return top_element

    def top(self):
        if self.isEmpty(): 
            print("stack id Empty")
            return -1

        return self.StackArray[self.topIndex]

    def isEmpty(self):
        return self.topIndex == -1


if __name__ == '__main__':
    # st = ArrayStack()
    stack = ArrayStack()
    commands = ["ArrayStack", "push", "push", "top", "pop", "isEmpty"]
    inputs = [[], [5], [10], [], [], []]
    
    for i in range(len(commands)):
        if commands[i] == "push":
            stack.push(inputs[i][0])
            print("null", end=" ")
    
        elif commands[i] == "pop":
            print(stack.pop(), end = " ")
    
        elif commands[i] == "top":
            print(stack.top(), end = " ")
    
        elif commands[i] == "isEmpty":
            print("true" if stack.isEmpty() else "false")
    
        elif commands[i] == "ArrayStack":
            print("null", end= " ")
    












    
            