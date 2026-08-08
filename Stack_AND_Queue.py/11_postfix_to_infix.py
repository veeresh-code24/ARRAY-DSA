# Function to convert postfix to infix
def postfix_to_infix(postfix):
    stack = []

    # Traverse the postfix expression from left to right
    for c in postfix:
        # If the character is an operand, push it to the stack
        if c.isalnum():
            stack.append(c)
        else:
            # Pop two operands from the stack
            op2 = stack.pop()
            op1 = stack.pop()

            # Form the new infix expression and push back to stack
            stack.append(f"({op1}{c}{op2})")

    # The final element in the stack is the result
    return stack[-1]


# Main function for testing
def main():
    postfix = "AB*C+"
    print("Infix Expression:", postfix_to_infix(postfix))


if __name__ == "__main__":
    main()

def postfix_to_infix(postfix):
    stack = []

    for c in postfix:
        if c.isalnum():
            stack.append(c)

        else:

            op2 = stack.pop()
            op1 = stack.pop()

            stack.append(f"({op1}{c}{op2})")


    return stack[-1]

if __name__ == '__main__':
    post = "AB+C*"

    print(f"Infix Expression: {post}")
    print(postfix_to_infix(post))









