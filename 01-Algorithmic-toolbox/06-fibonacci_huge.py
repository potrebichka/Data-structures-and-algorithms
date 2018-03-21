#python3

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

# using pisano period - period with which the sequence of Fibonacci numbers taken modulo n repeats
def get_fibonacci_huge(n, m):
    pisano_number = 0
    if n <= 1:
        return n % m
    
    count = 0
    previous = 0
    current  = 1
    while True:
        previous, current = current, (previous + current)
        count += 1
        if (previous % m) == 0 and (current % m) == 1:
            pisano_number = count
            break
        elif count == n-1:
            break
        else:
            "Error"

    if pisano_number <= 0:
        return current % m
    elif pisano_number > 0:
        k = n % pisano_number
        previous = 0
        current = 1
        for _ in range(k-1):
            previous, current = current, (previous + current)
        return current % m
        

inp = input()
n, m = map(int, inp.split())
print(get_fibonacci_huge(n, m))
