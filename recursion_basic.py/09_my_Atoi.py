# Brute Force

def myAtoi(s):
    i = 0

    # Skip leading spaces
    while i < len(s) and s[i] == ' ':
        i += 1

    # Check sign
    sign = 1
    if i < len(s) and (s[i] == '+' or s[i] == '-'):
        if s[i] == '-':
            sign = -1
        i += 1

    # Build the number
    num = 0
    while i < len(s) and s[i].isdigit():
        num = num * 10 + int(s[i])
        i += 1

    num *= sign

    # Clamp to 32-bit range
    if num < -2**31:
        return -2**31
    if num > 2**31 - 1:
        return 2**31 - 1

    return num

# Optimal Solution Recursion


'''INT_MIN = -2**31
INT_MAX = 2**31 - 1

def helper(s,i,num,sign):
    if i >= len(s) or not s[i].isdigit():
        return sign * num

    num = num * 10 + int(s[i])

    if sign * num <= INT_MIN: return INT_MIN
    if sign * num >= INT_MAX: return INT_MAX

    return helper(s, i+1, num,sign)

def myAtoi(s):
    i = 0

    while i < len(s) and s[i] == ' ':
        i += 1

    sign = 1
    if i < len(s) and (s[i] == '+' or s[i] == '-'):
        sign = -1 if s[i] == '-' else 1
        i += 1

    return helper(s, i, 0, sign)

if __name__ == "__main__":
    s = " -12345"
    print(myAtoi(s))
'''


INT_MIN = -2**31
INT_MAX = 2**31 -1

def helper(s,i,num,sign):

    if i >= len(s) or not s[i].isdigit():
        return sign * num

    num = num * 10 + int(s[i])

    if sign * num <= INT_MIN: return INT_MIN
    if sign * num >= INT_MAX: return INT_MAX

    return helper(s, i+1, num, sign)

def myAtoi(s):
    i = 0

    while i < len(s) and s[i] == ' ':
        i += 1


    sign = 1
    if i < len(s) and (s[i] == '+' or s[i] == '-'):
        sign -1 if s[i] == '-' else 1
        i += 1

    return helper(s,i, 0, sign)

if __name__ == "__main__":
    s = "  +12abc34"
    print(myAtoi(s))


# Optimal Solution (Iterative)

def myAtoi(s):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    i = 0
    n = len(s)

    # Skip leading spaces
    while i < n and s[i] == ' ':
        i += 1

    # Check sign
    sign = 1
    if i < n and (s[i] == '+' or s[i] == '-'):
        if s[i] == '-':
            sign = -1
        i += 1

    num = 0

    # Read digits
    while i < n and s[i].isdigit():
        digit = int(s[i])

        # Overflow check
        if num > (INT_MAX - digit) // 10:
            return INT_MAX if sign == 1 else INT_MIN

        num = num * 10 + digit
        i += 1

    return sign * num

