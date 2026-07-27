# Paremeterized

'''def fun(i,fact):
    if i < 1:
        print(fact)
        return 

    fun(i-1, fact*i)

def main():
    n = int(input("Enter the number: "))
    fun(n,1)

main()
'''
# function Call

# def fun(n):
#     if n == 1:
#         return 1

#     return n * fun(n-1)


# def main():
#     n = int(input("Enter the number: "))
#     print(fun(n))

# main()

''''def fun(i,fact):
    if i == 1:
        print(fact)
        return 


    fun(i-1,fact * i)


fun(5,1)
'''

def fun(n):
    if n == 1:
        return 1


    return n * fun(n-1)

print(fun(4))
    
