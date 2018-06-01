def move(n, a, b, c):
    if n == 1:
        print('move', n, a, '-->', c)
    else:
        move(n-1, a, c, b)
        print('move', n, a, '-->', c)
        move(n-1, b, a, c)

#test
move(4, 'A', 'B', 'C')