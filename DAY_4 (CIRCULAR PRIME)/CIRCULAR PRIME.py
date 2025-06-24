def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_rotations(n):
    rotations = []
    s = str(n)
    for i in range(len(s)):
        rotation = s[i:] + s[:i]
        rotations.append(int(rotation))
    return rotations

def is_circular_prime(n):
    rotations = get_rotations(n)
    for rotation in rotations:
        if not is_prime(rotation):
            return False
    return True

number = int(input ("Enter a number to check whether it is circular prime or not : "))
if is_circular_prime(number):
    print(f"{number} is a circular prime.")
else:
    print(f"{number} is not a circular prime.")
