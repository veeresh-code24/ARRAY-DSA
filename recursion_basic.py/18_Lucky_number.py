def is_lucky_number(n, counter):
    if n < counter:
        return True

    if n % counter == 0:
        return False

    return is_lucky_number(n-(n//counter), counter+1)

print(is_lucky_number(9, 2))