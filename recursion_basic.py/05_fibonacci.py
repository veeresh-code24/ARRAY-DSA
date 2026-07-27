'''def fun(n):
    if n == 1 or n == 2:
        return 1
    
    if n <= 1:
        return n
    
    return fun(n-1) + fun(n-2)

def main():
    n = int(input())
    print(fun(n))

main()'''


# def fun(n):
#     if n <= 1:
#         return 1

#     return fun(n-1) + fun(n-2)


# print(fun(4))

def fun(n):
    if n == 1 or n == 2:
        return 1

    return fun(n-1) + fun(n-2)


print(fun(6))

