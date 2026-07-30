'''def count_digits(n):
    if n < 10:
        return 1

    return 1 + count_digits(n//10)


print(count_digits(1))

def count_digits(n):
    if n == 0:
        return 1

    count = 0

    while n > 0:
        count += 1
        n = n // 10

    return count


print(count_digits(12345))


def count_digits(n):
    n = abs(n)

    if n == 0:
        return 1

    count = 0

    while n > 0:
        count += 1
        n //= 10

    return count


print(count_digits(-9876))  # 4
print(count_digits(0))      # 1'''

# def sum_of_digit(i,sum):
#     if i < 1:
#         print(sum)
#         return

#     sum_of_digit(i-1,sum+i)

# sum_of_digit(10,0)

def sum_of_digit(n):
    if n < 1:
        return 0

    return n + sum_of_digit(n-1)

print(sum_of_digit(5))






