# Infinite Recursion

'''import time
def fun():
    print(1)
    time.sleep(0.2)

    fun ()

fun()'''

# Base condition

'''def fun(cnt):

    if cnt == 3:
        return 
    

    print(cnt)
    cnt += 1

    fun(cnt)


def main():
    fun(0)


if __name__ == '__main__':
    main()'''

# Print Name N times

'''def fun(i,n):

    if i == n:
        return 
    
    print("Iranna")
    fun(i+1,n)

n = 5
fun(0,n)'''

# Print Linearly from 1 to N

'''def fun(i,n):

    if i > n:
        return 
    
    print(i)
    fun(i+1,n)


n = 4
fun(1,n)'''

# Print in terms N to 1

'''def fun(i,n):
    if i < 1:
        return
    print(i)
    fun(i-1,n) 

def main():
    n = int(input("Rnter the number:"))
    fun(n,n)

if __name__ == '__main__':
    main()'''

# Print Linearly from 1 to N (But By Backtracking)

'''def fun(i,n):
    if i < 1:
        return
    
    fun(i-1,n)
    print(i)


def main():
    n = int(input("Enter the number: "))
    fun(n,n)

if __name__ == '__main__':
    main()'''

# Print Linearly from N to 1 (But By Backtracking)

'''def fun(i,n):
    if i > n:
        return 
    
    fun(i+1,n)
    print(i)


def main():
    n = int(input("Enter the number: "))
    fun(1,n)

if __name__ == "__main__":
    main()'''

# Sum Of First N numbers ---paramaterzied recursion---
# Work happens while going down

'''def fun(i,sum):
    if i < 1:
        print(sum)
        return
    
    fun(i-1,sum+i)

def main():
    n = int(input("Enter the number: "))
    fun(n,0)

if __name__ == '__main__':
    main()'''

# Functional Recursion
# Work happens while coming back

def fun(i):
    if i == 0:
        return 0
    
    return i + fun(i-1)

n = int(input())
print(fun(n))



    







    





