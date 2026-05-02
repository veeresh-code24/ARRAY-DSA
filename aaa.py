'''def fun(i,n):
    if i > n:
        return 
    
    print("Iranna")
    fun(i+1,n)
n = 5
fun(1,n)'''

# def fun(i,n):
#     if i > n:
#         return 
#     print(i)
#     fun(i+1,n)

# def main():
#     n = int(input("Enter the number: "))
#     fun(1,n)

# if __name__ == '__main__':
#     main()

'''def fun(i,n):
    if i < 1:
        return
    
    print(i)
    fun(i-1,n)


def main():
    n = int(input("Enter the number: "))
    fun(n,n)

if __name__ == '__main__':
    main()'''

# def fun(i,n):
#     if i < 1:
#         return 
#     fun(i-1,n)
#     print(i)

# def main():
#     n = int(input("Enter the number: "))
#     fun (n,n)

# if __name__ == '__main__':
#     main()

# def fun(i,n):
#     if i > n:
#         return

#     fun(i+1,n)
#     print(i)

# def main():
#     n = int(input("Enter thr nmber: "))
#     fun(1,n)

# if __name__ == '__main__':
#     main()

# def fun(i):
#     if i == 3:
#         return
    
#     print(i)
#     i += 1
#     fun(i)

# fun(0)

# def fun(i):
#     if i == 0:
#         return
#     print("Iranna")
#     fun (i-1)

# fun(3)

# def fun(i,n):
#     if i == 0:
#         return 
    
#     print(i)
#     fun(i-1,n)
# n = 3
# fun(3,n)

# def fun(i,n):
#     if i >= n:
#         return
    
#     print("Iranna")
#     fun(i+1,n)
# n = 25
# fun(0,n)


# def fun(i,n):
#     if i > n:
#         return
#     print(i)
#     fun(i+1,n)

# n = 5
# fun(1,n)

# def fun(i,n):
#     if i < 1:
#         return
#     print(i)
#     fun(i-1,n)
# n = 5
# fun(n,n)

# def fun(i,n):
#     if i < 1:
#         return
#     fun(i-1,n)
#     print(i)

# n = 5
# fun(5,n)

# n = 5
# def fun(i):
#     if i > n:
#         return
    
#     fun(i+1)
#     print(i)

# fun(1)


def binary_search(nums,target):
    n = len(nums)
    low,high = 0,n-1

    while low <= high:
        mid = (low+high)//2

        if nums[mid] == target:
            return mid
        
        elif nums[mid] > target:
            high = mid-1

        else:
            low = mid+1

    return -1

nums = [3,4,6,7,9,12,16,17]
target = 17
print(binary_search(nums,target))

    



