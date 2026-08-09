def prefix_to_postfix(prefix):
    stack = []

    for i in range(len(prefix)-1, -1, -1):
        if prefix[i].isalnum():
            stack.append(prefix[i])

        else:
            top2 = stack.pop()
            top1 = stack.pop()
            stack.append(f"{top2}{top1}{prefix[i]}")

    return stack[-1]

if __name__ == "__main__":
    prefix = "/-AB*+DEF"
    print(f"prefix expression: {prefix}")
    print(prefix_to_postfix(prefix))