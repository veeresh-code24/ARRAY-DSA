# using parameterized

'''def fun(i,sum):
    if i < 1:
        print(sum)
        return
    
    fun(i-1, sum + i)


def main():
    n = int(input("Enter the number: "))
    fun(n,0)

main()'''

# using a functional 


def fun(n):
    if n == 0:
        return 0
    
    return n+fun(n-1)

def main():
    n = 2
    print(fun(n))

main()
