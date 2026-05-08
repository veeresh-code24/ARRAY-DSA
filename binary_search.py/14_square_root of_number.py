# Brute Approach

def square_root_of_number(n):
    ans = 1
    for i in range(1,n):
        if i * i <= n:
            ans = i

        else:
            break

    return ans

n = 27
print(square_root_of_number(n))


# Optimal Approach

def square_of_number(n):
    low,high = 1,n
    ans = 1

    while low <= high:
        mid = (high+low)//2

        if (mid**mid) <= n:
            ans = mid
            low = mid+1

        else:
            high = mid - 1

    return ans


n = 36
print(square_of_number(n))


