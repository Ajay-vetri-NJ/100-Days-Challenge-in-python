n = 5
for i in range(1, n+1):
    # printing spaces
    for j in range(n - i):
        print(' ', end='')

    # printing stars
    for k in range(2 * i - 1):
        # print star at start and end of the row
        if k == 0 or k == 2 * i - 2:
            print('*', end='')
        else:
            if i == n:
                print('*', end='')
            else:
                print(' ', end='')
    print()