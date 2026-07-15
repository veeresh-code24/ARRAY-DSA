# Infinite Recursion

'''import time
def fun():
    print(1)
    time.sleep(0.2)

    fun ()

fun()'''

# INFINITE Recursion

'''def f():
    print(1)
    f()

def main():
    f()

main()'''


# With a Base Condition

'''cnt = 0
def f():
    global cnt
    if (cnt==3):
        return 
    
    print(cnt)
    cnt += 1

    f()
def main():
    f()

main()'''

'''def f(cnt):
    if cnt == 10:
        return
    print(cnt)

    f(cnt + 1)


f(0)'''

# Print name 5 times

'''def f(name):
    if name == 5:
        return 
    
    print("Iranna")
    f(name + 1)

f(0)'''


# Print N Times

'''def f(i,n):
    if (i > n):
        return 
    
    print("Iranna")
    f(i+1, n)


n = int(input("enter a number"))
f(1,n)'''

# Print 1 to N

'''def f(i,n):
    if i > n:
        return 
    
    print(i)
    f(i+1,n)

def main():
    n = int(input("Enter the numbers"))
    f(1,n)

main()'''

# Print N to 1

'''def f(i,n):
    if i < 1:
        return
    
    print(i)
    f(i-1, n)

def main():
    n = int(input("Enter the number: "))
    f(10,n)

main()'''

# BACKTRACKING N to 1

'''def f(i,n):
    if i > n:
        return 
    
    f(i+1,n)
    print(i)

def main():
    n = int(input("Enter the number: "))
    f(1,n)

main()'''

# BACKTRACKING 1 TO N

def f(i,n):
    if i < 1:
        return 
    
    f(i-1,n)
    print(i)


def main():
    n = int(input("Enter the Number: "))
    f(n,n)

main()




    
    



