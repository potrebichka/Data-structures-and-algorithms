#python3
# The goal in this problem is to find the last digit of a sum of the first n Fibonacci numbers

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current)
        sum += current

    return sum % 10

def fibonacci_sum(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    # for modulo = 10
    pisano_number = 60
    # new variable
    k = n % pisano_number
    
    for _ in range(k +1):
        previous, current = current, (previous + current)

    return (current-1)%10
	
inp = input()
n = int(inp)
print(fibonacci_sum(n))
