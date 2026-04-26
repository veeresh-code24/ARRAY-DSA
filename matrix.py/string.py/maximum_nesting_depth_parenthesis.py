def nesting_dep_pare(s):
    max_depth = 0
    curre_dept = 0

    for char in s:
        if char == "(":
            curre_dept += 1

            max_depth = max(max_depth, curre_dept)


        elif char == ")":
            curre_dept -= 1

    return max_depth

s = "(1+(2*3)+((8)/4))+1"
# s = "(1)+((2))+(((3)))"
# s = "()(())((()()))"

print(nesting_dep_pare(s))