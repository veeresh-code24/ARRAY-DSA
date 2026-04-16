def outermost_parenthesis(s):

    result = ""
    level = 0

    for char in s:

        if char == "(":

            if level > 0:
                result += char

            level += 1

        elif char == ")":

            level -= 1

            if level > 0:
                result += char


    return result

# s =  "(()())(())(()(()))"
# s = "()()"
s = "(()())(())"

print(outermost_parenthesis(s))