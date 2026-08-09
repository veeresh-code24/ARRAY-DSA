def postfix_to_prefix(postfix):
    stack = []

    for c in postfix:
        if c.isalnum():
            stack.append(c)
        else:
            top2 = stack.pop()
            top1 = stack.pop()
            stack.append(f"{c}{top1}{top2}")

    return stack[-1]

if __name__ == "__main__":
    postfix = "AB-DE+F*/"
    print("postfix expression", {postfix})
    print(postfix_to_prefix(postfix))