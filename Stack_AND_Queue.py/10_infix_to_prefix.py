# Reverse the infix
# infix to postfix
# reverse the answer

# Function to get priority of operators
'''def getPriority(operator):

    if operator == '^':
        return 3

    elif operator == '/' or operator == '*':
        return 2

    elif operator == '+' or operator == '-':
        return 1

    else:
        return 0


# Infix to Postfix
def infixtoPostfix(infix):

    infix = '(' + infix + ')'

    stack = []
    res = ""

    for c in infix:

        # Operand
        if c.isalnum():
            res += c

        # Opening bracket
        elif c == '(':
            stack.append('(')

        # Closing bracket
        elif c == ')':

            while stack and stack[-1] != '(':
                res += stack.pop()

            stack.pop()

        # Operator
        else:

            while stack and getPriority(c) <= getPriority(stack[-1]):
                res += stack.pop()

            stack.append(c)

    while stack:
        res += stack.pop()

    return res


# Infix to Prefix
def infixPrefix(infix):

    # 1. Reverse the infix
    infix = infix[::-1]

    # 2. Swap brackets
    infix = infix.replace('(', 'temp').replace(')', '(').replace('temp', ')')

    # 3. Convert to postfix
    prefix = infixtoPostfix(infix)

    # 4. Reverse the postfix answer
    return prefix[::-1]


# Main
if __name__ == "__main__":

    exp = "(p+q)*(c-d)"

    print(f"Infix expression: {exp}")
    print(f"Prefix Expression: {infixPrefix(exp)}")

def getPriority(operator):

    if operator == '^':
        return 3

    elif operator == '/' or operator == '*':
        return 2
    elif operator == '+'or operator == '-':
        return 1

    else:
        return 0

def infixtoPostfix(infix):
    infix = '(' + infix + ')'
    stack = []
    res = ""
    for c in infix:

        if c.isalnum():
            res += c

        elif c == '(':
            stack.append('(')

        elif c == ')':

            while stack and stack[-1] != '(':
                res += stack.pop()

            stack.pop()

        else:
            while stack and getPriority(c) <= getPriority(stack[-1]):
                res += stack.pop()

            stack.append(c)


    while stack:
        res += stack.pop()

    return res


def infixPrefix(infix):
    infix = infix[::-1]

    infix = infix.replace('(', 'temp').replace (')' , '(').replace('temp', ')')

    prefix = infixtoPostfix(infix)

    return prefix[::-1]

if __name__ == '__main__':
    exp = "(p+q)*(c-d)"
    print("Infix expression: {exp}")
    print(f"prefix Expeesiion : {infixPrefix(exp)}")

'''





