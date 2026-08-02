def tower_of_hanoi(n, src,aux, dest):
    if n == 1:
        print(src, '-->', dest)
        return

    tower_of_hanoi(n-1,src, dest, aux)
    tower_of_hanoi(1, src, aux, dest)
    tower_of_hanoi(n-1, aux, src, dest)


tower_of_hanoi(4,'A', 'B', 'C')


