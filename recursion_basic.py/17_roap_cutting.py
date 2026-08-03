def max_pieces(n,a,b,c):
    pieces = 0
    if n == 0:
        return 0

    elif n < 0:
        return -1

    temp1 = max_pieces(n-a, a, b, c)
    temp2 = max_pieces(n-b, a, b, c)
    temp3 = max_pieces(n-c, a, b, c)
    pieces = max(temp1, temp2, temp3)

    if pieces == -1:
        return -1
    return pieces + 1

print(max_pieces(15, 5, 7, 8))



    