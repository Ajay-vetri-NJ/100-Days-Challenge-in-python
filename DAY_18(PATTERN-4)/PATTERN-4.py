size = int(input("Enter the size: "))

for i in range(size):
    for j in range(i):
        print(' ', end='')
    for j in range(2 * (size - i - 1) + 1):
        print('*', end='')
    print()